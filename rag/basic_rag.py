"""
rag/basic_rag.py - 简易 RAG 检索增强生成示例
"""
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
)

# 模拟知识库
KNOWLEDGE_BASE = [
    {"id": 1, "text": "Python 是一种解释型、面向对象的高级编程语言。"},
    {"id": 2, "text": "RAG 全称 Retrieval-Augmented Generation，结合检索与生成。"},
    {"id": 3, "text": "向量数据库用于存储嵌入向量并支持相似度搜索。"},
]

def embed(text: str) -> list[float]:
    """获取文本嵌入向量"""
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )
    return resp.data[0].embedding

def retrieve(query: str, top_k: int = 2):
    """检索最相关的文档（简化版：用长度近似相似度）"""
    # 真实场景应使用向量相似度计算
    q_len = len(query)
    scored = [(abs(len(d["text"]) - q_len), d) for d in KNOWLEDGE_BASE]
    scored.sort(key=lambda x: x[0])
    return [d for _, d in scored[:top_k]]

def generate(query: str):
    """基于检索结果生成回答"""
    docs = retrieve(query)
    context = "\n".join(f"[{d['id']}] {d['text']}" for d in docs)

    response = client.chat.completions.create(
        model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": f"参考以下资料回答问题：\n{context}"},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    q = "什么是 RAG？"
    print(f"🔍 问题: {q}")
    print("🤖 回答:", generate(q))
