"""
llm/chat.py - 最简单的 LLM 对话示例
使用前请先配置 .env 文件中的 OPENAI_API_KEY
"""
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
)

def chat(messages, model=None):
    """发送对话请求并返回回复"""
    model = model or os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "你是一个简洁友好的AI助手。"},
        {"role": "user", "content": "你好！用三句话介绍一下什么是AI Agent。"},
    ]
    answer = chat(messages)
    print("🤖:", answer)
