import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from backend.agent_council.gemini_rotator import gemini_rotator

prompt = """Hãy sinh 3 câu hỏi trắc nghiệm Lịch sử Việt Nam chuẩn cấu trúc ĐGNL ĐHQG.
Chủ đề: Giai đoạn 1945 - 1975.
Trả về định dạng JSON array:
[
  {
    "prompt": "Nội dung câu hỏi...",
    "passage": null,
    "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
    "correct_answer": "A",
    "explanation": "Giải thích...",
    "difficulty": "medium"
  }
]"""

for model in ["gemini-2.0-flash", "gemini-1.5-flash"]:
    print(f"\n--- Testing model: {model} ---")
    gemini_rotator.model = model
    ok, text, key = gemini_rotator.generate_content(prompt, response_json=True, max_output_tokens=2000)
    print(f"Model: {model} -> Success: {ok}, Key mask: {key}")
    if ok:
        print(f"Sample output ({len(text)} chars): {text[:200]}")
