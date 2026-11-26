import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import httpx
from backend.agent_council.gemini_rotator import gemini_rotator

gemini_rotator.reload_keys()
keys = gemini_rotator.keys
print(f"Testing all {len(keys)} keys with 'gemini-flash-lite-latest'...")

working = 0
for i, k in enumerate(keys):
    mask = f"...{k[-6:]}"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key={k}"
    payload = {
        "contents": [{"parts": [{"text": "Hi"}]}],
        "generationConfig": {"maxOutputTokens": 5}
    }
    try:
        r = httpx.post(url, json=payload, timeout=6.0)
        if r.status_code == 200:
            working += 1
            print(f"[{i+1}/{len(keys)}] Key {mask}: 200 OK")
        else:
            print(f"[{i+1}/{len(keys)}] Key {mask}: HTTP {r.status_code}")
    except Exception as e:
        print(f"[{i+1}/{len(keys)}] Key {mask}: Error: {e}")

print(f"\nResult: {working}/{len(keys)} keys working with gemini-flash-lite-latest!")
