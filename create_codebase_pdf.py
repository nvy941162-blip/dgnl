import subprocess
from pathlib import Path

PROJECT_DIR = Path("D:/Antigravity/Dang gia nang luc")
HTML_PATH = PROJECT_DIR / "tailieu_giaithich_code_multiagent.html"
PDF_PATH = PROJECT_DIR / "TAI_LIEU_GIAI_THICH_MA_NGUON_MULTIAGENT_KHKT.pdf"

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = f"file:///{HTML_PATH.resolve().as_posix()}"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_PATH}",
    file_url
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and PDF_PATH.exists():
    print(f"SUCCESS: Generated PDF at {PDF_PATH} ({PDF_PATH.stat().st_size} bytes)")
else:
    print(f"Error: {res.stderr}")
