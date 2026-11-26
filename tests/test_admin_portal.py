import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_admin_portal():
    print("\n--- 1. Testing Admin Seed & Login ---")
    # Trigger student list to ensure admin seed
    stus_resp = client.get("/api/auth/students")
    assert stus_resp.status_code == 200
    
    # Login as admin
    admin_login = client.post("/api/auth/login", json={
        "username": "admin",
        "password": "admin123"
    })
    print("Admin login status:", admin_login.status_code)
    assert admin_login.status_code == 200
    admin_data = admin_login.json()["user"]
    print("Admin info:", admin_data)
    assert admin_data["role"] == "admin"

    print("\n--- 2. Testing Admin User List ---")
    users_resp = client.get("/api/admin/users")
    assert users_resp.status_code == 200
    all_users = users_resp.json()["users"]
    print(f"Total registered users (including admin): {len(all_users)}")
    assert len(all_users) >= 1
    assert any(u["username"] == "admin" for u in all_users)

    print("\n--- 3. Testing Create Student and Admin Password Reset ---")
    client.post("/api/auth/register", json={
        "username": "student_temp_test",
        "password": "old_password_123",
        "full_name": "Lê Văn Tạm",
        "student_class": "12A3",
        "school": "THPT Lê Quý Đôn"
    })
    
    # Lấy thông tin học sinh vừa tạo
    users_resp = client.get("/api/admin/users")
    temp_user = next(u for u in users_resp.json()["users"] if u["username"] == "student_temp_test")
    temp_id = temp_user["id"]
    print("Created temp student id:", temp_id)

    # Admin reset password
    reset_resp = client.post(f"/api/admin/users/{temp_id}/reset-password", json={
        "new_pass": "new_secret_888"
    })
    assert reset_resp.status_code == 200
    print("Password reset status:", reset_resp.json()["message"])

    # Verify student can login with new password
    login_new = client.post("/api/auth/login", json={
        "username": "student_temp_test",
        "password": "new_secret_888"
    })
    assert login_new.status_code == 200
    print("Student logged in with new reset password successfully!")

    print("\n--- 4. Testing Admin Delete Student ---")
    del_resp = client.delete(f"/api/admin/users/{temp_id}")
    assert del_resp.status_code == 200
    print("Deleted temp student:", del_resp.json()["message"])

    # Verify cannot login anymore
    login_del = client.post("/api/auth/login", json={
        "username": "student_temp_test",
        "password": "new_secret_888"
    })
    assert login_del.status_code == 401
    print("Deleted student cannot login (401 Unauthorized verified)!")

    # Verify admin cannot delete admin
    admin_id = admin_data["id"]
    del_admin = client.delete(f"/api/admin/users/{admin_id}")
    assert del_admin.status_code == 400
    print("Protected root admin from deletion: 400 Bad Request verified!")

    print("\n>>> ALL ADMIN PORTAL & MANAGEMENT TESTS PASSED 100%! <<<")

if __name__ == "__main__":
    test_admin_portal()
