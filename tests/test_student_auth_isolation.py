import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from backend.app import app
from backend.database import init_db, get_db, UserModel, SubmissionModel

client = TestClient(app)

def test_auth_and_isolation():
    print("\n--- 1. Testing Student Registration ---")
    reg_resp = client.post("/api/auth/register", json={
        "username": "student_test_a",
        "password": "123",
        "full_name": "Nguyễn Văn A",
        "student_class": "12A1",
        "school": "THPT Chuyên"
    })
    print("Register Status:", reg_resp.status_code)
    # 200 or 400 if exists
    assert reg_resp.status_code in [200, 400]
    
    print("\n--- 2. Testing Student Login ---")
    login_resp = client.post("/api/auth/login", json={
        "username": "student_test_a",
        "password": "123"
    })
    assert login_resp.status_code == 200
    user_a = login_resp.json()["user"]
    print("Logged in user A:", user_a)
    assert user_a["username"] == "student_test_a"

    # Register student B
    client.post("/api/auth/register", json={
        "username": "student_test_b",
        "password": "456",
        "full_name": "Trần Thị B",
        "student_class": "12A2",
        "school": "THPT Nguyễn Trãi"
    })
    login_b = client.post("/api/auth/login", json={"username": "student_test_b", "password": "456"}).json()["user"]
    print("Logged in user B:", login_b)

    print("\n--- 3. Testing Exam Submission Linked to Student A ---")
    # Submit exam for user A
    sub_resp = client.post("/api/exams/vact_sample_2026/submit", json={
        "candidate_name": user_a["full_name"],
        "user_id": user_a["id"],
        "answers": {"1": "A", "2": "B"},
        "time_spent_seconds": 120
    })
    assert sub_resp.status_code == 200
    sub_id_a = sub_resp.json()["submission_id"]
    print("Submitted exam for user A, Sub ID:", sub_id_a)

    print("\n--- 4. Testing History Isolation ---")
    # History for user A
    hist_a = client.get(f"/api/history?user_id={user_a['id']}").json()["history"]
    print(f"History count for User A: {len(hist_a)}")
    assert any(h["id"] == sub_id_a for h in hist_a)

    # History for user B should NOT contain user A's exam
    hist_b = client.get(f"/api/history?user_id={login_b['id']}").json()["history"]
    print(f"History count for User B: {len(hist_b)}")
    assert not any(h["id"] == sub_id_a for h in hist_b)
    print("SUCCESS: User B CANNOT see User A's submission in history!")

    print("\n--- 5. Testing Direct Submission View Security ---")
    # User A can view own submission
    view_a = client.get(f"/api/submissions/{sub_id_a}?user_id={user_a['id']}")
    assert view_a.status_code == 200
    print("User A view own submission: 200 OK")

    # User B tries to view User A's submission -> must be 403 Forbidden
    view_b = client.get(f"/api/submissions/{sub_id_a}?user_id={login_b['id']}")
    print("User B view User A submission status code:", view_b.status_code)
    assert view_b.status_code == 403
    print("SUCCESS: 403 Forbidden returned when User B tries to inspect User A's exam!")

    print("\nALL STUDENT AUTH & DATA ISOLATION TESTS PASSED 100%!")

if __name__ == "__main__":
    test_auth_and_isolation()
