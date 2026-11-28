import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import json
from fastapi.testclient import TestClient
from backend.app import app

def test_live_api():
    client = TestClient(app)

    print("================ LIVE API SYSTEM INTEGRITY TEST ================")

    # 1. Test Root and Static frontend
    r = client.get("/")
    assert r.status_code == 200, f"Root / failed: {r.status_code}"
    assert "ĐGNL Assessment Platform" in r.text or "Hệ Thống Tạo Đề" in r.text, "Index HTML missing title"
    print("[✓] Endpoint GET /: OK (Frontend served properly)")

    # 2. Test Get Exams List
    r = client.get("/api/exams")
    assert r.status_code == 200, f"Exams list failed: {r.status_code}"
    exams = r.json()
    assert isinstance(exams, list) and len(exams) >= 10, f"Exams count too low: {len(exams)}"
    print(f"[✓] Endpoint GET /api/exams: OK ({len(exams)} exams returned)")

    # 3. Test Student Register & Login
    test_uname = "stu_audit_2026"
    client.post("/api/auth/register", json={
        "username": test_uname,
        "password": "password123",
        "full_name": "Thí Sinh Khảo Thí",
        "student_class": "12A1",
        "school": "THPT Chuyên"
    })

    r_login_stu = client.post("/api/auth/login", json={"username": test_uname, "password": "password123"})
    assert r_login_stu.status_code == 200, f"Student login failed: {r_login_stu.text}"
    stu_data = r_login_stu.json()["user"]
    assert stu_data.get("role") == "student", "Role should be student"
    print(f"[✓] Endpoint POST /api/auth/login (Student): OK ({stu_data['full_name']})")

    r_login_adm = client.post("/api/auth/login", json={"username": "admin", "password": "admin123"})
    assert r_login_adm.status_code == 200, f"Admin login failed: {r_login_adm.text}"
    adm_data = r_login_adm.json()["user"]
    assert adm_data.get("role") == "admin", "Role should be admin"
    print(f"[✓] Endpoint POST /api/auth/login (Admin): OK ({adm_data['full_name']})")

    # 4. Test Exams Detail & Submission across diverse types
    test_targets = [
        {"desc": "V-ACT 120 câu chuẩn ĐHQG-HCM", "filter": lambda e: e.get("exam_type") == "vact"},
        {"desc": "SPT Toán ĐH Sư Phạm Hà Nội", "filter": lambda e: e.get("exam_type") == "spt" and e.get("subject") == "math"},
        {"desc": "SPT Tiếng Anh ĐH Sư Phạm Hà Nội", "filter": lambda e: e.get("exam_type") == "spt" and e.get("subject") == "english"},
        {"desc": "SPT GDKT&PL ĐH Sư Phạm Hà Nội", "filter": lambda e: e.get("exam_type") == "spt" and e.get("subject") == "civics_law"},
    ]

    for target in test_targets:
        match_exam = next((e for e in exams if target["filter"](e)), None)
        assert match_exam is not None, f"Could not find exam for {target['desc']}"
        ex_id = match_exam["id"]

        # GET detail
        r_detail = client.get(f"/api/exams/{ex_id}")
        assert r_detail.status_code == 200, f"Get detail failed for {ex_id}"
        detail = r_detail.json()
        questions = detail.get("questions", [])
        assert len(questions) > 0, f"Exam {ex_id} has 0 questions"

        # Giả lập trả lời 50% câu hỏi để kiểm tra chấm điểm đa chiều
        answers = {}
        for idx, q in enumerate(questions):
            q_num = str(q.get("question_number", idx + 1))
            q_type = q.get("question_type", "multiple_choice")
            c_ans = q.get("correct_answer")
            if idx % 2 == 0: # Trả lời đúng
                answers[q_num] = c_ans
            else: # Trả lời khác hoặc bỏ trống
                answers[q_num] = "A" if q_type == "multiple_choice" else None

        # POST submit
        sub_payload = {
            "user_id": stu_data["id"],
            "answers": answers,
            "time_spent_seconds": 1800
        }
        r_sub = client.post(f"/api/exams/{ex_id}/submit", json=sub_payload)
        assert r_sub.status_code == 200, f"Submit failed for {ex_id}: {r_sub.text}"
        sub_res = r_sub.json()

        assert "grade_report" in sub_res, "Missing grade_report"
        assert "competency_analysis" in sub_res, "Missing competency_analysis"
        assert "radar_image" in sub_res, "Missing radar_image"
        assert sub_res["radar_image"].startswith("data:image/png;base64,"), "Radar image not valid base64"

        grade = sub_res["grade_report"]
        comp = sub_res["competency_analysis"]

        print(f"[✓] Submit '{target['desc']}':")
        print(f"    - Total Score: {grade['total_score']} / {grade['max_total_score']} (is_spt={grade.get('is_spt')})")
        print(f"    - Subscores: P1={grade.get('sec1_score')}, P2={grade.get('sec2_score')}, P3={grade.get('sec3_score')}")
        print(f"    - Competency Tier: {comp.get('tier_rating')[:50]}... (Percentile: {comp.get('estimated_percentile')}%)")
        print(f"    - Radar Chart: Valid Base64 Image ({len(sub_res['radar_image'])} chars)")

    # 5. Test Admin students endpoint
    r_students = client.get("/api/auth/students")
    assert r_students.status_code == 200, "Get students failed"
    stu_list = r_students.json().get("students", [])
    assert len(stu_list) > 0, "Empty students list"
    print(f"[✓] Endpoint GET /api/auth/students: OK ({len(stu_list)} students)")

    print("\n🎉 LIVE API TEST SUITE: 100% HOÀN HẢO, TẤT CẢ CÁC ĐẦU MÚT ĐỀU HOẠT ĐỘNG CHUẨN XÁC! 🎉")

if __name__ == "__main__":
    test_live_api()
