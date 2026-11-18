import os
import sys
from pathlib import Path

# Thêm thư mục gốc dự án vào sys.path để có thể import module backend
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from backend.app import app

# Export app cho Vercel ASGI runtime
handler = app
