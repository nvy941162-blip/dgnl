import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx
from backend.agent_council.gemini_rotator import gemini_rotator

gemini_rotator.reload_keys()
key = gemini_rotator.keys[0]
print(f"Testing key: ...{key[-6:]}")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
resp = httpx.get(url)
print(f"Status: {resp.status_code}")
if resp.status_code == 200:
    data = resp.json()
    models = [m["name"] for m in data.get("models", []) if "generateContent" in m.get("supportedGenerationMethods", [])]
    print("Supported models for generateContent:")
    for m in models:
        print(" -", m)
else:
    print(resp.text)
