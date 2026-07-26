"""
tests/test_utils.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.text import chunk_text, clean_text

def test_chunk_text():
    text = "a" * 550
    chunks = chunk_text(text, chunk_size=200, overlap=20)
    assert len(chunks) >= 3
    print(f"  ✅ chunk_text: {len(chunks)} chunks")

def test_clean_text():
    assert clean_text("  hello   world  ") == "hello world"
    print("  ✅ clean_text passed")

if __name__ == "__main__":
    test_chunk_text()
    test_clean_text()
    print("🎉 全部测试通过！")
