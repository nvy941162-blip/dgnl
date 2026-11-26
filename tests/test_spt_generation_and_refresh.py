import sys
import time
import json as json_module
import os
import urllib.request
import urllib.error

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

class Resp:
    def __init__(self, status, content):
        self.status_code = status
        self._content = content
    def json(self):
        return json_module.loads(self._content)

def get_client():
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
                                return Resp(r.status, r.read().decode('utf-8'))
                        except urllib.error.HTTPError as e:
                            return Resp(e.code, e.read().decode('utf-8'))

                    def post(self, path, json_data=None):
                        data = json_module.dumps(json_data).encode('utf-8') if json_data is not None else None
                        req = urllib.request.Request(f"http://127.0.0.1:8050{path}", data=data, headers={"Content-Type": "application/json"} if json_data is not None else {}, method="POST")
                        try:
                            with opener.open(req) as r:
                                return Resp(r.status, r.read().decode('utf-8'))
                        except urllib.error.HTTPError as e:
                            return Resp(e.code, e.read().decode('utf-8'))

                    def delete(self, path):
                        req = urllib.request.Request(f"http://127.0.0.1:8050{path}", method="DELETE")
                        try:
                            with opener.open(req) as r:
                                return Resp(r.status, r.read().decode('utf-8'))
                        except urllib.error.HTTPError as e:
                            return Resp(e.code, e.read().decode('utf-8'))

                return LiveClient()
    except Exception:
        pass

    from fastapi.testclient import TestClient
    from backend.app import app
    print("[OK] Sử dụng FastAPI TestClient (In-Process)")
    class WrappedTestClient:
        def __init__(self, c):
            self.c = c
        def get(self, path):
            return self.c.get(path)
        def post(self, path, json_data=None):
            return self.c.post(path, json=json_data)
        def delete(self, path):
            return self.c.delete(path)
    return WrappedTestClient(TestClient(app))

def test_spt_generation_and_counts():
    client = get_client()

    expected_counts = {
        "spt_math": 25,
        "spt_english": 33,
        "spt_chemistry": 27,
        "spt_geography": 20,
        "spt_history": 25,
        "spt_civics": 21,
        "spt_tech_ind": 24,
        "spt_tech_agr": 24,
    }

    created_exam_ids = []

    print("\n--- 1. KIỂM TRA SINH ĐỀ TỪNG MÔN SPT (ĐÚNG SỐ LƯỢNG CÂU HỎI, KHÔNG SINH 120 CÂU) ---")
    for mode, expected_total in expected_counts.items():
        print(f"\nKiểm tra sinh đề mode: {mode} (Kỳ vọng: {expected_total} câu)...")
        res = client.post("/api/exams/generate-120", json_data={
            "title": f"Đề thi thử SPT kiểm thử - {mode}",
            "theme": "Chương trình GDPT 2018",
            "mode": mode
        })
        assert res.status_code == 200, f"Lỗi gọi sinh đề {mode}: {res.status_code}"
        task_id = res.json()["task_id"]

        exam_id = None
        for _ in range(40):
            time.sleep(0.3)
            st_res = client.get(f"/api/exams/generate-120/status/{task_id}")
            assert st_res.status_code == 200
            st_data = st_res.json()
            if st_data["status"] == "completed":
                exam_id = st_data["exam_id"]
                assert st_data["total_count"] == expected_total, f"total_count sai: {st_data['total_count']} != {expected_total}"
                break
            elif st_data["status"] == "failed":
                raise RuntimeError(f"Tạo đề thất bại: {st_data.get('error')}")

        assert exam_id is not None, f"Không tạo được đề {mode}"
        created_exam_ids.append(exam_id)

        # Lấy đề từ database qua API
        exam_detail = client.get(f"/api/exams/{exam_id}?mode=test")
        assert exam_detail.status_code == 200
        d = exam_detail.json()
        actual_questions = len(d["questions"])
        print(f" -> Kết quả: Đề {exam_id} có {actual_questions} câu hỏi, thời gian {d['duration_minutes']} phút, thang điểm {d['max_score']}")
        assert actual_questions == expected_total, f"Số câu hỏi {actual_questions} != {expected_total}"
        assert actual_questions != 120, "LỖI: Đang sinh 120 câu thay vì đúng số lượng câu của môn!"
        assert d["max_score"] == 10.0, f"Thang điểm SPT phải là 10.0, nhận được: {d['max_score']}"

    print("\n--- 2. KIỂM TRA CHẤM ĐIỂM ĐỀ SPT MỚI SINH RA ---")
    test_math_id = created_exam_ids[0]
    sub_res = client.post(f"/api/exams/{test_math_id}/submit", json_data={
        "candidate_name": "Thí sinh SPT Test",
        "answers": {"1": "A", "2": "B", "3": "C"},
        "time_spent_seconds": 1200
    })
    assert sub_res.status_code == 200
    sub_data = sub_res.json()
    total_score = sub_data["grade_report"]["total_score"]
    max_score = sub_data["grade_report"]["max_total_score"]
    print(f" -> Điểm chấm: {total_score} / {max_score} điểm (Thang 10.0)")
    assert max_score == 10.0
    assert 0 <= total_score <= 10.0

    print("\n--- 3. KIỂM TRA LOGIC REFRESH TRANG (KIỂM TRA ĐỀ CÒN HAY ĐÃ BỊ XÓA) ---")
    # Kiểm tra khi đề còn tồn tại -> trả về 200 để phòng thi tự động khôi phục
    chk_exist = client.get(f"/api/exams/{test_math_id}?mode=test")
    assert chk_exist.status_code == 200
    print(f" -> Đề {test_math_id} còn tồn tại: HTTP 200 OK (Giao diện thi tiếp tục mở, không thoát)")

    # Xóa đề thi
    del_res = client.delete(f"/api/exams/{test_math_id}")
    assert del_res.status_code == 200
    print(f" -> Đã xóa đề {test_math_id}: HTTP 200 OK")

    # Kiểm tra sau khi xóa -> trả về 404 để frontend tự động clear session và thoát ra dashboard
    chk_deleted = client.get(f"/api/exams/{test_math_id}?mode=test")
    assert chk_deleted.status_code == 404
    print(f" -> Đề đã xóa: HTTP 404 Not Found (Frontend tự động hủy session thi và thoát về dashboard)")

    # Dọn dẹp các đề thử nghiệm còn lại
    for eid in created_exam_ids[1:]:
        client.delete(f"/api/exams/{eid}")

    print("\n🎉 TOÀN BỘ CÁC KIỂM THỬ ĐÃ THÀNH CÔNG 100%!")

if __name__ == "__main__":
    test_spt_generation_and_counts()
