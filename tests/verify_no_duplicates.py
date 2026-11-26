import os, sys, json, time
sys.stdout.reconfigure(line_buffering=True)
sys.path.insert(0, ".")

from backend.database import SessionLocal, ExamModel
from backend.exam_engine.spt_sample_data import ALL_SPT_SAMPLE_EXAMS
from backend.agent_council.full_exam_generator import full_exam_generator

# 1. Tìm đề mẫu môn Toán
sample_math = next(e for e in ALL_SPT_SAMPLE_EXAMS if e.get("subject") == "math" or "toán" in e.get("title", "").lower())
sample_prompts = [q["prompt"].strip() for q in sample_math["questions"]]

print(f"Sample Math has {len(sample_prompts)} questions.")
print(f"Sample Q1 prompt: {sample_prompts[0][:100]}")

# 2. Sinh một đề thi mới bằng full_exam_generator
task_id = full_exam_generator.generate_full_exam_async(
    exam_title="Đề Thi Kiểm Tra Độ Trùng Lặp Môn Toán",
    topic_theme="Hàm số bậc ba, Tích phân và Hình học Oxyz",
    mode="spt_math"
)
print("Started generation task:", task_id)

from backend.agent_council.full_exam_generator import GENERATION_TASKS
for sec in range(90):
    time.sleep(1)
    task = GENERATION_TASKS.get(task_id, {})
    if sec % 5 == 0:
        print(f"  [{sec}s] Status: {task.get('status')} | Progress: {task.get('percent')}% | Step: {task.get('current_step')}")
    if task.get("status") in ["completed", "failed"]:
        break

print("Task final status:", task.get("status"), "Exam ID:", task.get("exam_id"))
exam_id = task.get("exam_id")
assert exam_id, f"Generation failed: {task.get('error')}"

# 3. Lấy đề vừa sinh từ Database
db = SessionLocal()
new_exam = db.query(ExamModel).filter(ExamModel.id == exam_id).first()
new_questions = json.loads(new_exam.data_json)
db.close()

print(f"Generated exam has {len(new_questions)} questions.")

# 4. So sánh từng câu hỏi
duplicates = []
for i, q in enumerate(new_questions):
    prompt_clean = q["prompt"].strip()
    if prompt_clean in sample_prompts:
        duplicates.append((i + 1, prompt_clean))
    else:
        if i < 3:
            print(f"\n[Generated Q{i+1}]: {prompt_clean[:120]}")
            print(f"  Options: {q.get('options')}")
            print(f"  Correct: {q.get('correct_answer')}")

print("\n" + "=" * 50)
print(f"SỐ CÂU TRÙNG LẶP NGUYÊN MẪU VỚI ĐỀ MẪU: {len(duplicates)} / {len(new_questions)}")
if len(duplicates) == 0:
    print(">>> TUYỆT VỜI! 100% CÂU HỎI MỚI HOÀN TOÀN KHÔNG BỊ TRÙNG VỚI ĐỀ MẪU! <<<")
else:
    print("Các câu bị trùng:", duplicates)
print("=" * 50)
