import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import httpx
from backend.agent_council.gemini_rotator import gemini_rotator

gemini_rotator.reload_keys()
keys = gemini_rotator.keys
print(f"Total keys loaded: {len(keys)}")

working_keys = []
for i, k in enumerate(keys):
    mask = f"...{k[-6:]}"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={k}"
    payload = {
        "contents": [{"parts": [{"text": "Reply with 'OK'."}]}],
        "generationConfig": {"maxOutputTokens": 10}
    }
    try:
        r = httpx.post(url, json=payload, timeout=8.0)
        if r.status_code == 200:
            print(f"[{i+1}/{len(keys)}] Key {mask}: OK (200)")
            working_keys.append(k)
        elif r.status_code == 404:
            # Check models for this key
            print(f"[{i+1}/{len(keys)}] Key {mask}: 404 (model not available for this key)")
        elif r.status_code == 429:
            print(f"[{i+1}/{len(keys)}] Key {mask}: 429 (Rate limited/Quota)")
        else:
            print(f"[{i+1}/{len(keys)}] Key {mask}: HTTP {r.status_code}")
    except Exception as e:
        print(f"[{i+1}/{len(keys)}] Key {mask}: Timeout / Error: {e}")

print(f"\nTotal working keys with gemini-2.5-flash: {len(working_keys)}/{len(keys)}")
