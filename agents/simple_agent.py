"""
agents/simple_agent.py - 简易 AI Agent 示例（带工具调用）
"""
import json
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
)

# ===== 工具定义 =====
def get_weather(city: str) -> str:
    """获取指定城市的天气（模拟数据）"""
    fake_db = {"北京": "晴 25°C", "上海": "多云 28°C", "深圳": "阵雨 30°C"}
    return fake_db.get(city, f"{city}: 暂无数据")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的当前天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称"}
                },
                "required": ["city"],
            },
        },
    }
]

TOOL_MAP = {"get_weather": get_weather}

def run_agent(user_message: str):
    """运行 Agent 循环"""
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.chat.completions.create(
            model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
            messages=messages,
            tools=TOOLS,
        )
        msg = response.choices[0].message

        # 如果没有工具调用，返回最终回复
        if not msg.tool_calls:
            return msg.content

        # 执行工具调用
        messages.append(msg)
        for tc in msg.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            print(f"  🔧 调用工具: {name}({args})")
            result = TOOL_MAP[name](**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })

if __name__ == "__main__":
    answer = run_agent("帮我查一下深圳和北京的天气")
    print("🤖:", answer)
