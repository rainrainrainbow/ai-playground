# 🤖 ai-playground

> 🤖 一个 AI 实验与学习仓库：包含 LLM 调用、RAG、Agent 等示例代码

## ✨ 功能模块

| 目录 | 说明 |
|------|------|
| `llm/` | 大语言模型调用示例（OpenAI / Anthropic / 本地模型） |
| `rag/` | 检索增强生成（Retrieval-Augmented Generation） |
| `agents/` | AI Agent 与工具调用 |
| `notebooks/` | 实验性 Jupyter Notebook |
| `utils/` | 通用工具函数 |

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/rainrainrainbow/ai-playground.git
cd ai-playground

# 2. 创建虚拟环境
python -m venv .venv && source .venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 API Key

# 5. 运行示例
python llm/chat.py
```

## 📁 项目结构

```
ai-playground/
├── llm/              # LLM 调用封装
├── rag/              # 知识库检索
├── agents/           # Agent 框架
├── notebooks/        # 实验笔记
├── utils/            # 工具函数
├── tests/            # 单元测试
├── .env.example      # 环境变量模板
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🧪 示例代码

```python
# llm/chat.py
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是一个有帮助的AI助手"},
        {"role": "user", "content": "用一句话解释什么是RAG"}
    ]
)
print(response.choices[0].message.content)
```

## 📜 License

MIT License
