"""
utils/text.py - 文本处理工具
"""
import re
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """将长文本切分为重叠片段"""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start = end - overlap if end < len(text) else end
    return chunks

def clean_text(text: str) -> str:
    """清理文本：去除多余空白"""
    text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    sample = "人工智能 " * 200
    chunks = chunk_text(sample, chunk_size=100, overlap=20)
    print(f"原文长度: {len(sample)}，切分为 {len(chunks)} 个片段")
    for i, c in enumerate(chunks):
        print(f"  [{i}] len={len(c)}")
