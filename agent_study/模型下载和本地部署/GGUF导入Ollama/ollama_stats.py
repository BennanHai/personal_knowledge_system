"""本地 Ollama 模型健康检查、输出验证与每次会话的 token 统计。

前置条件：
    Ollama 服务已启动（默认 http://localhost:11434），且已安装 requests。

用法：
    uv run python ollama_stats.py --list
    uv run python ollama_stats.py --check
    uv run python ollama_stats.py --check --model xiaomi-ocr:q4
    uv run python ollama_stats.py --model xiaomi-ocr:q4 "用一句话介绍你自己"
    uv run python ollama_stats.py --model xiaomi-ocr:q4 --image "D:\\pics\\demo.png" "Extract the text in the image."
    uv run python ollama_stats.py --model xiaomi-ocr:q4            # 交互式多轮
    uv run python ollama_stats.py --report                         # 查看历史会话统计
"""

import argparse
import base64
import json
import sys
import time
import uuid
from pathlib import Path

import requests

DEFAULT_HOST = "http://localhost:11434"
LOG_PATH = Path(__file__).with_name("ollama_sessions.jsonl")


def _get(host: str, path: str, timeout: int = 10) -> dict:
    resp = requests.get(f"{host.rstrip('/')}{path}", timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def list_models(host: str) -> list[dict]:
    """服务健康检查 + 列出本地模型。"""
    version = _get(host, "/api/version")
    models = _get(host, "/api/tags").get("models", [])
    print(f"Ollama 版本: {version.get('version', 'unknown')}")
    if not models:
        print("没有已部署的模型")
        return []

    print(f"{'NAME':<28}{'SIZE':>8}  {'QUANT':<8}{'PARAMS':<10}FAMILY")
    for m in models:
        detail = m.get("details", {})
        size_gb = m.get("size", 0) / 1024**3
        print(
            f"{m['name']:<28}{size_gb:>7.2f}G  "
            f"{detail.get('quantization_level', '-'):<8}"
            f"{detail.get('parameter_size', '-'):<10}"
            f"{detail.get('family', '-')}"
        )
    return models


def turn_stats(data: dict, wall_seconds: float) -> dict:
    prompt_tokens = int(data.get("prompt_eval_count") or 0)
    output_tokens = int(data.get("eval_count") or 0)
    eval_ns = int(data.get("eval_duration") or 0)
    total_ns = int(data.get("total_duration") or 0)
    load_ns = int(data.get("load_duration") or 0)
    return {
        "prompt_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "tokens_per_sec": round(output_tokens / (eval_ns / 1e9), 2) if eval_ns else 0.0,
        "load_seconds": round(load_ns / 1e9, 2),
        "total_seconds": round(total_ns / 1e9, 2),
        "wall_seconds": round(wall_seconds, 2),
        "done_reason": data.get("done_reason", ""),
    }


def chat_turn(host: str, model: str, messages: list[dict], timeout: int = 600) -> tuple[str, dict]:
    """发送一轮对话，流式打印输出，返回 (完整文本, token 统计)。"""
    payload = {
        "model": model,
        "stream": True,
        "messages": messages,
        "options": {"temperature": 0, "num_ctx": 8192},
    }
    start = time.perf_counter()
    resp = requests.post(f"{host.rstrip('/')}/api/chat", json=payload, stream=True, timeout=timeout)
    resp.raise_for_status()

    parts: list[str] = []
    final: dict = {}
    for line in resp.iter_lines():
        if not line:
            continue
        data = json.loads(line)
        if data.get("error"):
            raise RuntimeError(data["error"])
        chunk = data.get("message", {}).get("content", "")
        if chunk:
            parts.append(chunk)
            print(chunk, end="", flush=True)
        if data.get("done"):
            final = data
            break
    print()

    return "".join(parts), turn_stats(final, time.perf_counter() - start)


def print_turn_stats(stats: dict, index: int | None = None) -> None:
    prefix = f"第 {index} 轮 | " if index else ""
    print(
        f"{prefix}prompt {stats['prompt_tokens']} tok | 输出 {stats['output_tokens']} tok | "
        f"{stats['tokens_per_sec']:.1f} tok/s | 加载 {stats['load_seconds']:.2f}s | "
        f"总耗时 {stats['total_seconds']:.2f}s"
    )


class Session:
    """一次脚本运行 = 一个会话，结束时把逐轮统计追加到 jsonl。"""

    def __init__(self, model: str, host: str, log_path: Path):
        self.id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
        self.model = model
        self.host = host
        self.log_path = log_path
        self.started_at = time.strftime("%Y-%m-%d %H:%M:%S")
        self.turns: list[dict] = []

    def add_turn(self, stats: dict) -> None:
        self.turns.append(stats)

    def totals(self) -> dict:
        prompt = sum(t["prompt_tokens"] for t in self.turns)
        output = sum(t["output_tokens"] for t in self.turns)
        eval_seconds = sum(
            t["output_tokens"] / t["tokens_per_sec"] for t in self.turns if t["tokens_per_sec"]
        )
        return {
            "turns": len(self.turns),
            "prompt_tokens": prompt,
            "output_tokens": output,
            "tokens_per_sec": round(output / eval_seconds, 2) if eval_seconds else 0.0,
        }

    def save(self) -> None:
        if not self.turns:
            return
        record = {
            "session_id": self.id,
            "started_at": self.started_at,
            "model": self.model,
            "host": self.host,
            "turns": self.turns,
            "totals": self.totals(),
        }
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"会话已记录：{self.log_path.name} [{self.id}]")


def build_message(prompt: str, image: str | None) -> dict:
    message: dict = {"role": "user", "content": prompt}
    if image:
        path = Path(image)
        if not path.is_file():
            raise FileNotFoundError(f"图片不存在：{path}")
        message["images"] = [base64.b64encode(path.read_bytes()).decode("utf-8")]
    return message


def run_one_shot(args, history: list[dict]) -> int:
    session = Session(args.model, args.host, Path(args.log))
    message = build_message(" ".join(args.prompt), args.image)
    history.append(message)
    _, stats = chat_turn(args.host, args.model, history)
    session.add_turn(stats)
    print_turn_stats(stats, 1)
    session.save()
    return 0


def run_interactive(args, history: list[dict]) -> int:
    session = Session(args.model, args.host, Path(args.log))
    print(f"模型 {args.model}，输入 /exit 结束会话，输入 /clear 清空上下文")
    index = 0
    while True:
        try:
            text = input("\n你> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not text:
            continue
        if text in {"/exit", "/quit"}:
            break
        if text == "/clear":
            history.clear()
            print("上下文已清空")
            continue

        index += 1
        history.append({"role": "user", "content": text})
        try:
            content, stats = chat_turn(args.host, args.model, history)
        except requests.ConnectionError:
            print("连接 Ollama 失败，请确认服务已启动：ollama serve", file=sys.stderr)
            return 1
        except requests.HTTPError as exc:
            print(f"请求失败：{exc}\n{exc.response.text}", file=sys.stderr)
            return 1
        history.append({"role": "assistant", "content": content})
        session.add_turn(stats)
        print_turn_stats(stats, index)

    if session.turns:
        totals = session.totals()
        print(
            f"\n会话合计：{totals['turns']} 轮 | prompt {totals['prompt_tokens']} tok | "
            f"输出 {totals['output_tokens']} tok | {totals['tokens_per_sec']:.1f} tok/s"
        )
        session.save()
    return 0


def check_model(host: str, model: str) -> int:
    """用一条固定提示词验证模型能否正常产出，并打印 token 统计。"""
    message = {"role": "user", "content": "Reply with exactly: OK"}
    print(f"冒烟测试：{model}")
    try:
        content, stats = chat_turn(host, model, [message], timeout=300)
    except requests.HTTPError as exc:
        print(f"FAIL 请求失败：{exc}\n{exc.response.text}", file=sys.stderr)
        return 1

    print_turn_stats(stats)
    ok = bool(content.strip()) and stats["output_tokens"] > 0
    print("PASS 模型有有效输出" if ok else "FAIL 模型输出为空")
    return 0 if ok else 1


def report(log_path: Path) -> int:
    if not log_path.is_file():
        print(f"暂无统计记录：{log_path}")
        return 0

    sessions = []
    with log_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                sessions.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not sessions:
        print("统计文件为空")
        return 0

    print(f"{'SESSION':<24}{'MODEL':<24}{'TURNS':>6}{'PROMPT':>9}{'OUTPUT':>9}{'TOK/S':>8}")
    for s in sessions:
        totals = s.get("totals", {})
        print(
            f"{s.get('session_id', '-'):<24}{s.get('model', '-'):<24}"
            f"{totals.get('turns', 0):>6}{totals.get('prompt_tokens', 0):>9}"
            f"{totals.get('output_tokens', 0):>9}{totals.get('tokens_per_sec', 0):>8.1f}"
        )

    by_model: dict[str, dict] = {}
    for s in sessions:
        key = s.get("model", "-")
        agg = by_model.setdefault(key, {"sessions": 0, "turns": 0, "prompt": 0, "output": 0})
        agg["sessions"] += 1
        agg["turns"] += s.get("totals", {}).get("turns", 0)
        agg["prompt"] += s.get("totals", {}).get("prompt_tokens", 0)
        agg["output"] += s.get("totals", {}).get("output_tokens", 0)

    print("\n按模型汇总：")
    for model, agg in by_model.items():
        print(
            f"  {model}: {agg['sessions']} 会话 / {agg['turns']} 轮 | "
            f"prompt {agg['prompt']} tok | 输出 {agg['output']} tok"
        )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ollama 模型健康检查与 token 统计")
    parser.add_argument("prompt", nargs="*", help="一次性提示词；不填且指定 --model 则进入交互模式")
    parser.add_argument("--model", help="模型名，如 xiaomi-ocr:q4")
    parser.add_argument("--image", help="图片路径，随首轮消息一起发送")
    parser.add_argument("--system", help="system 提示词")
    parser.add_argument("--list", action="store_true", dest="list_models", help="列出本地模型并检查服务")
    parser.add_argument("--check", action="store_true", help="健康检查；配合 --model 做冒烟测试")
    parser.add_argument("--report", action="store_true", help="汇总历史会话 token 统计")
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Ollama 地址，默认 {DEFAULT_HOST}")
    parser.add_argument("--log", default=str(LOG_PATH), help="会话统计 jsonl 路径")
    args = parser.parse_args()

    if args.list_models:
        try:
            list_models(args.host)
        except requests.ConnectionError:
            print("连接 Ollama 失败，请确认服务已启动：ollama serve", file=sys.stderr)
            return 1
        return 0

    if args.check:
        try:
            list_models(args.host)
        except requests.ConnectionError:
            print("连接 Ollama 失败，请确认服务已启动：ollama serve", file=sys.stderr)
            return 1
        return check_model(args.host, args.model) if args.model else 0

    if args.report:
        return report(Path(args.log))

    if not args.model:
        parser.error("聊天模式需要 --model，例如 --model xiaomi-ocr:q4")

    history: list[dict] = []
    if args.system:
        history.append({"role": "system", "content": args.system})

    try:
        if args.prompt:
            return run_one_shot(args, history)
        return run_interactive(args, history)
    except requests.ConnectionError:
        print("连接 Ollama 失败，请确认服务已启动：ollama serve", file=sys.stderr)
        return 1
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1
    except requests.HTTPError as exc:
        print(f"请求失败：{exc}\n{exc.response.text}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
