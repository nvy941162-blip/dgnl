import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def verify_complete_platform():
    print("==================================================")
    print("   KIỂM TRA NGHIỆM THU TOÀN DIỆN NỀN TẢNG ĐGNL    ")
    print("==================================================")

    # 1. Kiểm tra Admin & Student Auth
    print("\n[1/6] Kiểm tra Đăng nhập Admin & Phân quyền...")
    admin_login = client.post("/api/auth/login", json={"username": "admin", "password": "admin123"})
    assert admin_login.status_code == 200, "Admin login failed"
    admin_data = admin_login.json()["user"]
    assert admin_data["role"] == "admin"
    print("  -> Admin đăng nhập thành công:", admin_data["full_name"])

    # 2. Kiểm tra Học sinh Đăng ký & Đăng nhập
    print("\n[2/6] Kiểm tra Học sinh Đăng ký & Đăng nhập...")
    student_u = "test_eval_student"
    client.post("/api/auth/register", json={
        "username": student_u,
        "password": "password_123",
        "full_name": "Trần Đánh Giá",
        "student_class": "12A5",
        "school": "THPT Năng Khiếu"
    })
    stu_login = client.post("/api/auth/login", json={"username": student_u, "password": "password_123"})
    assert stu_login.status_code == 200
    stu_data = stu_login.json()["user"]
    print("  -> Học sinh đăng nhập thành công:", stu_data["full_name"])

    # 3. Kiểm tra Chặn Học sinh tạo đề (Chỉ Admin mới được tạo đề)
    print("\n[3/6] Kiểm tra Phân quyền tạo đề (Chặn học sinh, cho phép admin)...")
    stu_try_gen = client.post("/api/exams/generate-120", json={
        "title": "Đề Test Học Sinh",
        "mode": "spt_math",
        "user_id": stu_data["id"],
        "role": "student"
    })
    assert stu_try_gen.status_code == 403, "Học sinh không bị chặn tạo đề!"
    print("  -> ĐÃ CHẶN THÀNH CÔNG: Học sinh gọi tạo đề nhận HTTP 403 Forbidden!")

    admin_gen = client.post("/api/exams/generate-120", json={
        "title": "Đề Thử Nghiệm SPT Admin Môn Toán",
        "mode": "spt_math",
        "user_id": admin_data["id"],
        "role": "admin"
    })
    assert admin_gen.status_code == 200
    print("  -> ADMIN TẠO ĐỀ THÀNH CÔNG: HTTP 200 OK (Task ID:", admin_gen.json().get("task_id"), ")")

    # 4. Kiểm tra Học sinh nộp bài thi
    print("\n[4/6] Kiểm tra Học sinh làm bài và nộp bài thi...")
    sub_resp = client.post("/api/exams/vact_sample_2026/submit", json={
        "candidate_name": stu_data["full_name"],
        "user_id": stu_data["id"],
        "answers": {"1": "A", "2": "B", "3": "C"},
        "time_spent_seconds": 180
    })
    assert sub_resp.status_code == 200
    sub_data = sub_resp.json()
    sub_id = sub_data["submission_id"]
    print("  -> Nộp bài thành công! Điểm:", sub_data["grade_report"]["total_score"], "Mã bài làm:", sub_id)

    # 5. Kiểm tra Cô lập bài thi (Học sinh khác không thể xem)
    print("\n[5/6] Kiểm tra Bảo mật cô lập bài làm giữa các học sinh...")
    other_stu_id = "stu_other_dummy"
    inspect_resp = client.get(f"/api/submissions/{sub_id}?user_id={other_stu_id}")
    assert inspect_resp.status_code == 403
    print("  -> ĐÃ BẢO VỆ DỮ LIỆU: Thí sinh khác xem bài bị chặn 403 Forbidden!")

    # 6. Kiểm tra Bảng xếp hạng Admin (Từ cao xuống thấp) & Quyền Xóa bài thi
    print("\n[6/6] Kiểm tra Bảng vàng xếp hạng Admin & Chức năng Xóa bài làm...")
    lead_resp = client.get("/api/admin/leaderboard")
    assert lead_resp.status_code == 200
    leaderboard = lead_resp.json()["leaderboard"]
    assert len(leaderboard) > 0
    print(f"  -> Bảng xếp hạng hiện có {len(leaderboard)} bài làm.")
    print("  -> Thí sinh Top 1 hiện tại:", leaderboard[0]["candidate_name"], "-", leaderboard[0]["percentage"], "%")

    # Admin xóa bài làm vừa nộp
    del_sub = client.delete(f"/api/admin/submissions/{sub_id}")
    assert del_sub.status_code == 200
    print("  -> ADMIN XÓA BÀI LÀM THÀNH CÔNG:", del_sub.json()["message"])

    print("\n==================================================")
    print(">>> TẤT CẢ 6 HẠNG MỤC TÍNH NĂNG ĐÃ HOÀN THIỆN 100% <<<")
    print("==================================================")

if __name__ == "__main__":
    verify_complete_platform()
