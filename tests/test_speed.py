import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import time
import json
from backend.agent_council.gemini_rotator import gemini_rotator

gemini_rotator.model = "gemini-flash-lite-latest"

prompt = """Bạn là Tác tử chuyên môn ra đề thi ĐGNL ĐHQG.
Hãy tạo 5 câu hỏi trắc nghiệm Lịch Sử Việt Nam giai đoạn 1945 - 1975 hoàn toàn mới và chất lượng cao.
Trả về định dạng JSON array với các trường:
[
  {
    "prompt": "Câu hỏi...",
    "passage": null,
    "options": {
      "A": "Đáp án A",
      "B": "Đáp án B",
      "C": "Đáp án C",
      "D": "Đáp án D"
    },
    "correct_answer": "A",
    "explanation": "Giải thích chi tiết tại sao đúng...",
    "difficulty": "medium"
  }
]"""

t0 = time.time()
ok, text, key = gemini_rotator.generate_content(prompt, response_json=True, max_output_tokens=4000)
dur = time.time() - t0
print(f"Time: {dur:.2f}s | Success: {ok} | Key: {key}")
if ok:
    items = json.loads(text)
    print(f"Generated {len(items)} questions successfully!")
    print("Q1:", items[0]["prompt"])
    print("Options:", items[0]["options"])
    print("Ans:", items[0]["correct_answer"])
