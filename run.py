import uvicorn
import sys
import os
import threading
import time
import webbrowser

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Thêm thư mục gốc vào PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

port = int(os.getenv("PORT", "8050"))

def open_browser_delayed():
    time.sleep(1.5)
    url = f"http://localhost:{port}"
    try:
        webbrowser.open(url)
    except Exception:
        pass

if __name__ == "__main__":
    print("=" * 70)
    print(">>> DANG KHOI CHAY HE THONG TAO DE & THI THU DANH GIA NANG LUC (DGNL)")
    print(f">>> Web URL: http://localhost:{port}")
    print(">>> Cau truc de: 120 cau - 150 phut - Thang diem 1200 chuan DHQG")
    print(">>> Tich hop: LangGraph Multi-Agent, IRT Weighting, Radar Analytics")
    print("=" * 70)
    threading.Thread(target=open_browser_delayed, daemon=True).start()
    uvicorn.run("backend.app:app", host="127.0.0.1", port=port, reload=False)
