import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.agent_council.gemini_rotator import gemini_rotator

prompt = "Hello, reply with 1 short sentence."
for test_model in ["gemini-flash-latest", "gemini-2.5-flash-lite", "gemini-2.5-flash"]:
    print(f"\nTesting model: {test_model}")
    gemini_rotator.model = test_model
    gemini_rotator.reload_keys()
    ok, text, key = gemini_rotator.generate_content(prompt, max_output_tokens=50)
    print(f"Result for {test_model}: ok={ok}, key={key}, response={text[:60]}")
    if ok:
        break
