"""调用本地 Ollama 上的 Xiaomi-OCR-0 做图片 OCR / 文档解析。

前置条件：
    1. Ollama 服务已启动（默认 http://localhost:11434）
    2. 已执行 `ollama create xiaomi-ocr:q4 -f Modelfile` 导入模型
    3. 已安装 requests（本项目 pyproject 已包含）

用法：
    uv run python ocr_ollama.py "D:\\pics\\demo.png"
    uv run python ocr_ollama.py "D:\\pics\\demo.png" --task document
    uv run python ocr_ollama.py "D:\\pics\\demo.png" --task kie --prompt "你的 JSON schema"
    uv run python ocr_ollama.py "D:\\pics\\demo.png" --stream
"""

import argparse
import base64
import json
import sys
import time
from collections.abc import Iterator
from pathlib import Path

import requests

from ollama_stats import LOG_PATH, Session, print_turn_stats, turn_stats

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "xiaomi-ocr:q4"

# 官方模型卡给出的任务提示词
PROMPTS = {
    "text": "Extract the text in the image.",
    "document": (
        "Extract all information from the main body of the document image and represent it "
        "in markdown format, ignoring headers and footers. Tables should be expressed in OTSL "
        "format, formulas in the document should be represented using LATEX format, and the "
        "parsing should be organized according to the reading order."
    ),
    "table": "Parse the table in the image into OTSL.",
    "formula": "Identify the formula in the image and represent it using LATEX format.",
    "kie": "Extract key information in the image.",
}


def _prepare_request(
    image_path: str | Path,
    task: str,
    prompt: str | None,
    model: str,
    base_url: str,
    stream: bool,
) -> tuple[dict, str]:
    """校验参数并构造 /api/chat 请求体。"""
    path = Path(image_path)
    if not path.is_file():
        raise FileNotFoundError(f"图片不存在：{path}")

    prompt = prompt or PROMPTS.get(task)
    if prompt is None:
        raise ValueError(f"未知任务 {task}，可选：{', '.join(PROMPTS)}")

    image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")
    payload = {
        "model": model,
        "stream": stream,
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": [image_b64],
            }
        ],
        "options": {"temperature": 0, "num_ctx": 8192},
    }
    return payload, f"{base_url.rstrip('/')}/api/chat"


def ocr_image(
    image_path: str | Path,
    task: str = "text",
    prompt: str | None = None,
    model: str = DEFAULT_MODEL,
    base_url: str = OLLAMA_URL,
    timeout: int = 600,
    stats_out: dict | None = None,
) -> str:
    """非流式：一次性返回完整识别结果。"""
    payload, url = _prepare_request(image_path, task, prompt, model, base_url, stream=False)
    start = time.perf_counter()
    resp = requests.post(url, json=payload, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    if stats_out is not None:
        stats_out.update(turn_stats(data, time.perf_counter() - start))
    return data["message"]["content"]


def ocr_image_stream(
    image_path: str | Path,
    task: str = "text",
    prompt: str | None = None,
    model: str = DEFAULT_MODEL,
    base_url: str = OLLAMA_URL,
    timeout: int = 600,
    stats_out: dict | None = None,
) -> Iterator[str]:
    """流式：逐块 yield 识别结果文本。"""
    payload, url = _prepare_request(image_path, task, prompt, model, base_url, stream=True)
    start = time.perf_counter()
    resp = requests.post(url, json=payload, stream=True, timeout=timeout)
    resp.raise_for_status()
    final: dict = {}
    for line in resp.iter_lines():
        if not line:
            continue
        data = json.loads(line)
        if data.get("error"):
            raise RuntimeError(data["error"])
        chunk = data.get("message", {}).get("content", "")
        if chunk:
            yield chunk
        if data.get("done"):
            final = data
            break
    if stats_out is not None and final:
        stats_out.update(turn_stats(final, time.perf_counter() - start))


def print_summary(content: str) -> None:
    """打印 OCR 结果的简单摘要。"""
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    if not lines:
        print("输出摘要：无有效输出")
        return

    table_rows = sum(1 for line in lines if line.startswith("|"))
    formulas = content.count("$") // 2 + content.count("\\(")
    preview = lines[0] if len(lines[0]) <= 60 else lines[0][:60] + "..."
    print(
        f"输出摘要：{len(content)} 字符 / {len(lines)} 行 | "
        f"表格行 {table_rows} | 公式 {formulas} | 开头：{preview}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="调用本地 Ollama 的 Xiaomi-OCR-0 解析图片")
    parser.add_argument("image", help="图片路径")
    parser.add_argument(
        "--task",
        default="text",
        choices=sorted(PROMPTS),
        help="预设任务，默认 text",
    )
    parser.add_argument("--prompt", help="自定义提示词，覆盖 --task")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Ollama 模型名，默认 {DEFAULT_MODEL}")
    parser.add_argument("--url", default=OLLAMA_URL, help=f"Ollama 地址，默认 {OLLAMA_URL}")
    parser.add_argument("--stream", action="store_true", help="流式输出，逐块打印")
    args = parser.parse_args()

    stats: dict = {}
    content = ""
    try:
        if args.stream:
            parts: list[str] = []
            for chunk in ocr_image_stream(
                args.image,
                task=args.task,
                prompt=args.prompt,
                model=args.model,
                base_url=args.url,
                stats_out=stats,
            ):
                parts.append(chunk)
                print(chunk, end="", flush=True)
            print()
            content = "".join(parts)
        else:
            content = ocr_image(
                args.image,
                task=args.task,
                prompt=args.prompt,
                model=args.model,
                base_url=args.url,
                stats_out=stats,
            )
            print(content)
    except requests.ConnectionError:
        print("连接 Ollama 失败，请确认服务已启动：ollama serve", file=sys.stderr)
        return 1
    except (FileNotFoundError, ValueError) as exc:
        print(exc, file=sys.stderr)
        return 1
    except requests.HTTPError as exc:
        print(f"请求失败：{exc}\n{exc.response.text}", file=sys.stderr)
        return 1
    except RuntimeError as exc:
        print(f"生成失败：{exc}", file=sys.stderr)
        return 1

    print_summary(content)

    if stats:
        stats.update({"kind": "ocr", "task": args.task, "image": str(args.image)})
        print_turn_stats(stats, 1)
        session = Session(args.model, args.url, LOG_PATH)
        session.add_turn(stats)
        session.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
