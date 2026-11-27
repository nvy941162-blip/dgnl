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

    # 2. Sử dụng FastAPI TestClient in-process nếu chưa chạy uvicorn
    from fastapi.testclient import TestClient
    from backend.app import app
    print("[OK] Sử dụng FastAPI TestClient (In-Process)")

    class WrappedTestClient:
        def __init__(self, c):
            self._c = c
        def get(self, path):
            return self._c.get(path)
        def post(self, path, json_data=None):
            return self._c.post(path, json=json_data)
        def delete(self, path):
            return self._c.delete(path)

    return WrappedTestClient(TestClient(app))

def test_all_dhsp_hn_subjects():
    client = get_client()

    subjects_to_test = [
        ("spt_math", "Toán học", 25, 90, "Đại số, Giải tích, Hình học không gian, Lượng giác & Xác suất"),
        ("spt_english", "Tiếng Anh", 33, 60, "English Lexico-Grammar, Reading Comprehension & Writing"),
        ("spt_chemistry", "Hóa học", 27, 60, "Hóa học hữu cơ, Vô cơ, Tốc độ phản ứng, Cân bằng hóa học & Thực nghiệm"),
        ("spt_geography", "Địa lí", 20, 60, "Địa lí tự nhiên, Dân cư, Các vùng kinh tế trọng điểm & Biến đổi khí hậu"),
        ("spt_history", "Lịch sử", 25, 60, "Lịch sử Việt Nam hiện đại, Cách mạng giải phóng dân tộc & Hội nhập quốc tế"),
        ("spt_civics", "GDKT & Pháp luật", 21, 60, "Kinh tế thị trường, Pháp luật dân sự, Quyền bình đẳng & Trách nhiệm công dân"),
        ("spt_tech_ind", "Công nghệ Công nghiệp", 24, 60, "Cơ khí chế tạo, Bản vẽ kỹ thuật, Mạch điện tử & Công nghệ tự động hóa"),
        ("spt_tech_agr", "Công nghệ Nông nghiệp", 24, 60, "Nông nghiệp công nghệ cao, Lâm nghiệp sinh thái & Thủy sản bền vững")
    ]

    print("======================================================================")
    print("KIỂM THỬ ĐẶC TẢ SINH ĐỀ TẤT CẢ CÁC MÔN THI ĐẠI HỌC SƯ PHẠM HÀ NỘI (ĐHSP HN)")
    print("======================================================================")

    created_ids = []

    for mode, name, expected_q, expected_dur, theme in subjects_to_test:
        print(f"\n[TESTING] Sinh đề môn {name} (Kỳ vọng: {expected_q} câu, {expected_dur} phút, thang 10.0)...")
        res = client.post("/api/exams/generate-120", json_data={
            "title": f"Đề Tham Khảo SPT ĐH Sư Phạm Hà Nội - Môn {name}",
            "theme": theme,
            "mode": mode,
            "role": "admin"
        })
        assert res.status_code == 200, f"Lỗi POST /api/exams/generate-120: {res.status_code}"
        res_data = res.json()
        task_id = res_data["task_id"]
        assert res_data["mode"] == mode

        # Đợi tiến trình LangGraph hoàn tất
        completed = False
        task_info = None
        for _ in range(40):
            time.sleep(0.3)
            st_res = client.get(f"/api/exams/generate-120/status/{task_id}")
            assert st_res.status_code == 200
            st_data = st_res.json()
            if st_data["status"] == "completed":
                completed = True
                task_info = st_data
                break
            elif st_data["status"] == "failed":
                raise RuntimeError(f"Tạo đề thất bại: {st_data.get('error')}")

        assert completed, f"Tác vụ sinh đề {name} bị timeout!"
        exam_id = task_info["exam_id"]
        created_ids.append(exam_id)

        # 1. Kiểm tra số lượng câu hỏi và thời gian từ tác vụ
        assert task_info["total_count"] == expected_q, f"LỖI: Số câu {task_info['total_count']} != {expected_q}"
        assert task_info["duration_minutes"] == expected_dur, f"LỖI: Thời gian {task_info['duration_minutes']} != {expected_dur}"

        # 2. Kiểm tra chi tiết đề trong CSDL
        exam_res = client.get(f"/api/exams/{exam_id}?mode=test")
        assert exam_res.status_code == 200
        exam_detail = exam_res.json()
        actual_q_count = len(exam_detail["questions"])
        actual_dur = exam_detail["duration_minutes"]
        actual_max = exam_detail["max_score"]
        
        print(f"  ✓ Đã sinh thành công đề '{exam_detail['title']}'")
        print(f"  ✓ Số câu hỏi thực tế: {actual_q_count} câu (Chuẩn: {expected_q} câu - KHÔNG PHẢI 120 CÂU)")
        print(f"  ✓ Thời gian làm bài: {actual_dur} phút (Chuẩn: {expected_dur} phút)")
        print(f"  ✓ Thang điểm chuẩn: {actual_max} điểm")
        
        assert actual_q_count == expected_q
        assert actual_dur == expected_dur
        assert actual_max == 10.0

        # 3. Kiểm tra Multi-Agent Council logs
        agent_names = [log["agent"] for log in task_info.get("agent_logs", [])]
        print(f"  ✓ Hội đồng tác tử đã tham gia ({len(agent_names)} bước): {', '.join(set(agent_names))}")
        assert any("Specialist" in a or "Agent" in a for a in agent_names)

    # 4. Kiểm tra cơ chế tự sửa tiêu đề và nhận diện môn khi gửi nhầm tiêu đề V-ACT cũ
    print("\n[TESTING] Kiểm tra tự động nhận diện môn và sửa tiêu đề khi gửi nhầm 'Đề Thi ĐGNL Số 24'...")
    auto_res = client.post("/api/exams/generate-120", json_data={
        "title": "Đề Thi ĐGNL Số 24 - Luyện Thi Bứt Phá Điểm Số",
        "theme": "Đại số, Giải tích, Hình học không gian, Lượng giác & Xác suất",
        "mode": "spt_math"
    })
    assert auto_res.status_code == 200
    auto_task = auto_res.json()
    assert "Toán" in auto_task["resolved_title"]
    assert "ĐGNL Số" not in auto_task["resolved_title"]
    print(f"  ✓ Backend đã tự động chuẩn hóa tiêu đề thành: '{auto_task['resolved_title']}'")

    # Đợi tác vụ tự sửa hoàn tất
    for _ in range(40):
        time.sleep(0.3)
        st_res = client.get(f"/api/exams/generate-120/status/{auto_task['task_id']}")
        if st_res.status_code == 200 and st_res.json()["status"] == "completed":
            auto_exam_id = st_res.json()["exam_id"]
            created_ids.append(auto_exam_id)
            break

    # 5. Kiểm tra kỳ thi V-ACT (120 câu, 150 phút, thang 1200 điểm IRT)
    print("\n[TESTING] Kiểm tra sinh đề V-ACT 120 câu (Kỳ vọng: 120 câu, 150 phút, thang 1200.0)...")
    vact_res = client.post("/api/exams/generate-120", json_data={
        "title": "Đề Thi ĐGNL Số 99 - Thử Nghiệm V-ACT",
        "theme": "Khoa học, Xã hội & Đổi mới",
        "mode": "vact_full"
    })
    assert vact_res.status_code == 200
    vact_task = vact_res.json()
    for _ in range(50):
        time.sleep(0.3)
        st_res = client.get(f"/api/exams/generate-120/status/{vact_task['task_id']}")
        if st_res.status_code == 200 and st_res.json()["status"] == "completed":
            v_info = st_res.json()
            assert v_info["total_count"] == 120
            assert v_info["duration_minutes"] == 150
            v_detail = client.get(f"/api/exams/{v_info['exam_id']}?mode=test").json()
            assert len(v_detail["questions"]) == 120
            assert v_detail["duration_minutes"] == 150
            assert v_detail["max_score"] == 1200.0
            print(f"  ✓ V-ACT sinh đúng chuẩn: {len(v_detail['questions'])} câu, {v_detail['duration_minutes']} phút, {v_detail['max_score']} điểm.")
            client.delete(f"/api/exams/{v_info['exam_id']}")
            break

    # Dọn dẹp các đề thử nghiệm
    print("\n[CLEANUP] Dọn dẹp các đề thử nghiệm khỏi CSDL...")
    for eid in created_ids:
        client.delete(f"/api/exams/{eid}")
    print("  ✓ Đã dọn dẹp an toàn toàn bộ đề thử nghiệm.")

    print("\n🎉 XÁC NHẬN: TOÀN BỘ 8 MÔN ĐH SƯ PHẠM HÀ NỘI ĐỀU RA ĐÚNG SỐ LƯỢNG CÂU VÀ THỜI GIAN THEO ĐỀ MẪU CHUẨN 100%!")

if __name__ == "__main__":
    test_all_dhsp_hn_subjects()
