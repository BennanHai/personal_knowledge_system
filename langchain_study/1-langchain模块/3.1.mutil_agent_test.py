# -*- coding: utf-8 -*-
"""
5. 多轮对话 Agent 测试（基于本地 Ollama 部署的大模型）

知识点：
1. 使用 ChatOllama 调用本地 Ollama 模型
2. 使用 LangChain 1.x 的 create_agent 创建 Agent（模型 + 工具 + 系统提示词）
3. 通过维护 messages 历史列表，实现多轮对话（模型本身无状态，靠历史消息传递记忆）
4. Agent 可自主决定是否调用工具（查询时间 / 计算器）

运行前准备：
1. 启动 Ollama 服务：  ollama serve   （或直接运行 ollama run deepseek-r1:1.5b）
2. 确认模型已拉取：    ollama list
3. 运行本脚本：        uv run 5.mutil_agent_test.py
"""

import re

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

# ==================== 配置 ====================
# 换成你本地已拉取的任意模型即可，如 qwen3:4b、llama3.2:3b 等
MODEL_NAME = "deepseek-r1:1.5b"


# ==================== 定义工具 ====================
@tool
def get_current_time() -> str:
    """获取当前的日期和时间。当用户询问现在几点、今天日期时使用此工具。"""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def calculator(expression: str) -> str:
    """计算一个数学表达式并返回结果。表达式只支持加减乘除和括号，例如 (3 + 5) * 2。"""
    # 简单校验，只允许数字、运算符和括号，防止执行任意代码
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expression):
        return "错误：表达式包含非法字符"
    try:
        return str(eval(expression))  # noqa: S307 已通过白名单校验
    except Exception as e:
        return f"计算出错：{e}"


tools = [get_current_time, calculator]


# ==================== 创建 Agent ====================
def build_agent():
    model = ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        base_url="http://localhost:11434",  # Ollama 默认地址
    )
    return create_agent(
        model,
        tools=tools,
        system_prompt=(
            "你是一个乐于助人的中文助手。"
            "回答保持简洁准确。"
            "当需要知道当前时间或进行数学计算时，请调用提供的工具。"
        ),
    )


# ==================== 多轮对话循环 ====================
def strip_think(text: str) -> str:
    """deepseek-r1 系列模型的输出带有 <think>...</think> 思考过程，展示时去掉。"""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def main():
    agent = build_agent()
    # 关键：模型本身没有记忆，多轮对话 = 把历史消息列表一起传回给模型
    history = []

    print(f"已连接本地 Ollama 模型：{MODEL_NAME}")
    print("输入内容开始对话，输入 q 退出\n")

    while True:
        try:
            user_input = input("你: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if not user_input:
            continue
        if user_input.lower() in {"q", "quit", "exit"}:
            print("再见！")
            break

        history.append(HumanMessage(content=user_input))

        # 每轮都把「全部历史 + 最新输入」交给 Agent
        result = agent.invoke({"messages": history})
        history = result["messages"]  # Agent 返回的完整消息列表作为新历史

        # 取最后一条 AI 消息作为回答
        answer = next(
            (m for m in reversed(history) if isinstance(m, AIMessage) and m.content),
            "",
        )
        print(f"助手: {strip_think(str(answer))}\n")

    # 打印最终的消息历史，方便观察多轮对话的完整结构
    print("=" * 50)
    print(f"本次对话共 {len(history)} 条消息：")
    for m in history:
        role = {"human": "用户", "ai": "助手", "tool": "工具"}.get(m.type, m.type)
        preview = strip_think(str(m.content))[:80]
        print(f"  [{role}] {preview}")


if __name__ == "__main__":
    main()
 