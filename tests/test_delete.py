import sys
import os
import json
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
        return json.loads(self._content)

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
    return TestClient(app)

def test_delete_endpoints():
    client = get_client()

    # 1. Fetch exams
    resp = client.get("/api/exams")
    assert resp.status_code == 200, f"Get exams failed: {resp.status_code}"
    exams = resp.json()
    print(f"Tổng số đề thi trong DB: {len(exams)}")
    for e in exams[:5]:
        print(f"  - ID: {e['id']} | Title: {e['title'][:30]}... | Source: {e['source']}")

    # 2. Test deleting benchmark exam (MUST fail with 400)
    del_bench_resp = client.delete("/api/exams/dgnl_benchmark_standard_2025")
    assert del_bench_resp.status_code == 400, f"Benchmark exam should return 400, got {del_bench_resp.status_code}"
    print(f"SUCCESS: Đề Benchmark được bảo vệ an toàn! HTTP {del_bench_resp.status_code}")
    print(f"  Response: {del_bench_resp.json()}")

    # 3. Check if there are generated exams to delete
    ai_exams = [e for e in exams if e['source'] == 'langgraph_generated']
    print(f"Tìm thấy {len(ai_exams)} đề do AI sinh.")

    if ai_exams:
        target_exam = ai_exams[0]
        print(f"Kiểm tra xóa đề đơn lẻ: {target_exam['id']}")
        del_single_resp = client.delete(f"/api/exams/{target_exam['id']}")
        assert del_single_resp.status_code == 200
        print(f"SUCCESS: Xóa đề đơn lẻ thành công: {del_single_resp.json()}")

    # 4. Test bulk delete endpoint
    bulk_del_resp = client.delete("/api/exams-generated")
    assert bulk_del_resp.status_code == 200
    print(f"SUCCESS: Xóa hàng loạt đề AI: {bulk_del_resp.json()}")

    # 5. Verify benchmark still exists
    verify_resp = client.get("/api/exams")
    remaining = verify_resp.json()
    print(f"Số đề còn lại sau khi dọn dẹp: {len(remaining)}")
    assert any(e['id'] == 'dgnl_benchmark_standard_2025' for e in remaining), "Đề benchmark bị mất!"
    assert not any(e['source'] == 'langgraph_generated' for e in remaining), "Vẫn còn đề AI chưa bị xóa!"
    print("\n🎉 TẤT CẢ CÁC KIỂM THỬ XÓA ĐỀ ĐÃ ĐẠT CHUẨN 100%!")
    return True

if __name__ == "__main__":
    test_delete_endpoints()
