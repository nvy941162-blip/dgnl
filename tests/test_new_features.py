import sys
import time
import json
import os
import urllib.request
import urllib.error

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def get_client():
    # 1. Thử kết nối live server nếu đang chạy
    try:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open("http://127.0.0.1:8050/api/health", timeout=1.0) as resp:
            if resp.status == 200:
                print("[OK] Kết nối trực tiếp máy chủ đang chạy tại http://127.0.0.1:8050")
                class LiveClient:
                    def get(self, path):
                        req = urllib.request.Request(f"http://127.0.0.1:8050{path}")
                        try:
                            with opener.open(req) as r:
                                return type('Resp', (), {'status_code': r.status, 'json': lambda: json.loads(r.read().decode('utf-8'))})()
                        except urllib.error.HTTPError as e:
                            return type('Resp', (), {'status_code': e.code, 'json': lambda: json.loads(e.read().decode('utf-8'))})()

                    def post(self, path, json=None):
                        data = json.dumps(json).encode('utf-8') if json is not None else None
                        req = urllib.request.Request(f"http://127.0.0.1:8050{path}", data=data, headers={"Content-Type": "application/json"} if json is not None else {}, method="POST")
                        try:
                            with opener.open(req) as r:
                                return type('Resp', (), {'status_code': r.status, 'json': lambda: json.loads(r.read().decode('utf-8'))})()
                        except urllib.error.HTTPError as e:
                            return type('Resp', (), {'status_code': e.code, 'json': lambda: json.loads(e.read().decode('utf-8'))})()

                return LiveClient()
    except Exception:
        pass

    # 2. Sử dụng FastAPI TestClient in-process nếu chưa chạy uvicorn
    from fastapi.testclient import TestClient
    from backend.app import app
    print("[OK] Sử dụng FastAPI TestClient (In-Process)")
    return TestClient(app)

def run_tests():
    print("=== BẮT ĐẦU KIỂM THỬ TÍNH NĂNG MỚI ===")

    # 1. Kiểm tra Gemini Key Rotator
    print("\n1. Kiểm tra GeminiKeyRotator...")
    from backend.agent_council.gemini_rotator import GeminiKeyRotator
    rotator = GeminiKeyRotator()
    rotator.keys = ["FAKE_KEY_1", "FAKE_KEY_2", "FAKE_KEY_3"]
    for k in rotator.keys:
        rotator.key_status[k] = {"cooldown_until": 0.0, "failures": 0}

    k1, _ = rotator.get_available_key()
    k2, _ = rotator.get_available_key()
    k3, _ = rotator.get_available_key()
    print(f"Round Robin keys: {k1} -> {k2} -> {k3}")
    assert k1 == "FAKE_KEY_1" and k2 == "FAKE_KEY_2" and k3 == "FAKE_KEY_3"

    # Thử nghiệm đánh dấu lỗi Rate Limit 429 trên key 1
    rotator.mark_key_failure("FAKE_KEY_1", is_rate_limit=True)
    next_k, _ = rotator.get_available_key()
    print(f"Key tiếp theo sau khi Key 1 bị rate limit: {next_k}")
    assert next_k == "FAKE_KEY_2"
    print("[OK] GeminiKeyRotator hoạt động chính xác!")

    client = get_client()

    # 2. Kiểm tra API tạo đề 120 câu
    print("\n2. Kiểm tra API sinh trọn vẹn đề thi 120 câu (/api/exams/generate-120)...")
    res = client.post("/api/exams/generate-120", json={
        "title": "Đề Thi ĐGNL Số 02 - Tự Động AI",
        "theme": "Biến đổi khí hậu & Kinh tế số"
    })
    assert res.status_code == 200, f"Generate 120 failed: {res.status_code}"
    start_data = res.json()
    task_id = start_data["task_id"]
    print(f"Task ID khởi tạo: {task_id}")

    new_exam_id = None
    for attempt in range(60):
        time.sleep(0.8)
        st_res = client.get(f"/api/exams/generate-120/status/{task_id}")
        assert st_res.status_code == 200
        status_data = st_res.json()
        pct = status_data["percent"]
        step = status_data["current_step"]
        print(f"Tiến độ: {pct}% - {step}")
        if status_data["status"] == "completed":
            new_exam_id = status_data["exam_id"]
            print(f"[OK] Đã hoàn tất sinh đề 120 câu! Exam ID: {new_exam_id}")
            break
        elif status_data["status"] == "failed":
            raise RuntimeError(f"Tạo đề thất bại: {status_data.get('error')}")

    assert new_exam_id is not None, "Exam ID must be generated"

    # 3. Kiểm tra nạp đề thi mới để làm bài trực tiếp
    print("\n3. Kiểm tra nạp đề thi mới tạo trực tiếp vào phòng thi...")
    exam_res = client.get(f"/api/exams/{new_exam_id}?mode=test")
    assert exam_res.status_code == 200
    exam_data = exam_res.json()
    print(f"Tiêu đề đề thi: {exam_data['title']}")
    print(f"Số lượng câu hỏi trong đề: {len(exam_data['questions'])}")
    assert len(exam_data["questions"]) == 120, "Phải có đúng 120 câu hỏi"

    # 4. Kiểm tra nộp bài thi và chấm điểm trực tiếp trên đề mới tạo
    print("\n4. Kiểm tra nộp bài thi và chấm điểm theo trọng số IRT...")
    submit_payload = {
        "candidate_name": "Thí sinh Thử Nghiệm",
        "answers": {
            "1": "B", "2": "A", "41": "A", "61": "A", "71": "A", "81": "A", "91": "A", "101": "A", "111": "A"
        },
        "time_spent_seconds": 3800
    }
    sub_res = client.post(f"/api/exams/{new_exam_id}/submit", json=submit_payload)
    assert sub_res.status_code == 200
    sub_data = sub_res.json()
    print(f"Điểm tổng bài thi: {sub_data['grade_report']['total_score']} / 1200 điểm")
    print(f"Biểu đồ Radar dạng ảnh Base64: {'Có' if sub_data['radar_image'] else 'Không'}")
    print(f"Lời khuyên AI chuyên gia: {'Có' if sub_data['ai_advice'] else 'Không'}")
    print(f"Xếp loại năng lực: {sub_data['competency_analysis']['tier_rating']}")

    print("\n🎉 TẤT CẢ CÁC TÍNH NĂNG MỚI ĐÃ VƯỢT QUA KIỂM THỬ THÀNH CÔNG 100%!")
    return True

if __name__ == "__main__":
    run_tests()
