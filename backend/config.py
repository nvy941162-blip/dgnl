import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# App settings
APP_TITLE = "Hệ thống Tạo đề & Thi thử Đánh giá Năng lực (ĐGNL)"
APP_VERSION = "2.0.0"
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Paths & Vercel Serverless environment handling
IS_VERCEL = bool(os.getenv("VERCEL"))

if IS_VERCEL:
    import shutil
    DATA_DIR = Path("/tmp/data")
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    STATIC_DIR = Path("/tmp/static")
    STATIC_DIR.mkdir(parents=True, exist_ok=True)

    CHARTS_DIR = STATIC_DIR / "charts"
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    KNOWLEDGE_BASE_DIR = Path("/tmp/knowledge_base")
    KNOWLEDGE_BASE_DIR.mkdir(parents=True, exist_ok=True)

    DB_PATH = DATA_DIR / "dgnl_platform.db"

    # Sao chép file SQLite ban đầu từ source code sang /tmp để đảm bảo quyền ghi
    source_db = BASE_DIR / "data" / "dgnl_platform.db"
    if source_db.exists() and not DB_PATH.exists():
        try:
            shutil.copy2(source_db, DB_PATH)
        except Exception as e:
            print(f"Lỗi sao chép database lên /tmp: {e}")
else:
    DATA_DIR = BASE_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)

    STATIC_DIR = BASE_DIR / "static"
    STATIC_DIR.mkdir(exist_ok=True)

    CHARTS_DIR = STATIC_DIR / "charts"
    CHARTS_DIR.mkdir(exist_ok=True)

    KNOWLEDGE_BASE_DIR = BASE_DIR / "backend" / "knowledge_base"
    KNOWLEDGE_BASE_DIR.mkdir(parents=True, exist_ok=True)

    DB_PATH = DATA_DIR / "dgnl_platform.db"

FRONTEND_DIR = BASE_DIR / "frontend"

# LLM Configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

GEMINI_API_KEYS = os.getenv("GEMINI_API_KEYS", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "") or os.getenv("GOOGLE_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-lite-latest")

# Standard Exam Parameters
EXAM_DURATION_MINUTES = 150
TOTAL_QUESTIONS = 120
MAX_TOTAL_SCORE = 1200

# Sub-section max scores (ĐHQG HCM Standard: 400 - 300 - 500 = 1200)
SCORE_DISTRIBUTION = {
    "section_1_language": 400.0,       # 40 câu (20 TV + 20 TA)
    "section_2_logic_data": 300.0,     # 30 câu (10 Toán + 10 Logic + 10 Số liệu)
    "section_3_problem_solving": 500.0 # 50 câu (10 Hóa + 10 Lý + 10 Sinh + 10 Sử + 10 Địa)
}
