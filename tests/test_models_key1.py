import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import httpx
from backend.agent_council.gemini_rotator import gemini_rotator

gemini_rotator.reload_keys()
key = gemini_rotator.keys[0]
print(f"Testing key 1: ...{key[-6:]}")

models_to_test = [
    "gemini-2.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash",
    "gemini-flash-lite-latest",
    "gemini-3.1-flash-lite"
]

for m in models_to_test:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={key}"
    payload = {
        "contents": [{"parts": [{"text": "Say hi."}]}],
        "generationConfig": {"maxOutputTokens": 10}
    }
    try:
        r = httpx.post(url, json=payload, timeout=6.0)
        print(f"Model {m}: HTTP {r.status_code}")
        if r.status_code == 200:
            print("  SUCCESS! Text:", r.json()["candidates"][0]["content"]["parts"][0]["text"])
        else:
            print("  Error:", r.text[:120])
    except Exception as e:
        print(f"Model {m} error: {e}")
