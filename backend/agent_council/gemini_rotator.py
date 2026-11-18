import os
import time
import json
import threading
from typing import List, Dict, Any, Optional, Tuple
import httpx
from backend.config import BASE_DIR

class GeminiKeyRotator:
    """
    Module Quản lý & Xoay Vòng Gemini API Key (Key Pool Manager)
    - Tự động nạp nhiều key từ .env (GEMINI_API_KEYS=key1,key2,key3 hoặc GEMINI_API_KEY_1...)
    - Xoay vòng Round-Robin khi thực hiện các yêu cầu sinh nội dung
    - Tự động phát hiện lỗi 429 (ResourceExhausted / RateLimit) hoặc lỗi hạn mức (QuotaExceeded)
      để kích hoạt Auto-failover sang key kế tiếp ngay lập tức
    - Đặt thời gian hạ nhiệt (cooldown) cho key bị giới hạn để không gây nghẽn
    """
    def __init__(self):
        self.lock = threading.Lock()
        self.key_status: Dict[str, Dict[str, Any]] = {}
        self.current_index = 0
        from backend.config import GEMINI_MODEL
        self.model = GEMINI_MODEL or os.getenv("GEMINI_MODEL", "gemini-flash-lite-latest")
        self.reload_keys()

    def reload_keys(self) -> List[str]:
        """Nạp danh sách API keys từ môi trường và file .env"""
        keys = []
        
        # 1. Kiểm tra chuỗi danh sách ngăn cách bằng dấu phẩy
        raw_keys = os.getenv("GEMINI_API_KEYS", "")
        if raw_keys:
            for k in raw_keys.split(","):
                k_clean = k.strip()
                if k_clean and k_clean not in keys:
                    keys.append(k_clean)

        # 2. Kiểm tra các biến đánh số GEMINI_API_KEY_1, GEMINI_API_KEY_2,...
        for i in range(1, 21):
            k = os.getenv(f"GEMINI_API_KEY_{i}", "").strip()
            if k and k not in keys:
                keys.append(k)

        # 3. Kiểm tra biến đơn lẻ thông thường
        single_key = (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or "").strip()
        if single_key and single_key not in keys:
            keys.append(single_key)

        with self.lock:
            self.keys = keys
            for k in keys:
                if k not in self.key_status:
                    self.key_status[k] = {"cooldown_until": 0.0, "failures": 0}

        return self.keys

    def get_available_key(self) -> Optional[Tuple[str, int]]:
        """Lấy key khả dụng tiếp theo theo cơ chế round-robin và kiểm tra cooldown"""
        with self.lock:
            if not self.keys:
                return None
            
            now = time.time()
            total = len(self.keys)

            # Thử duyệt qua vòng tròn tìm key không bị cooldown
            for _ in range(total):
                key = self.keys[self.current_index]
                status = self.key_status.get(key, {"cooldown_until": 0.0})
                self.current_index = (self.current_index + 1) % total

                if now >= status.get("cooldown_until", 0.0):
                    return key, self.current_index

            # Nếu tất cả key đều đang trong thời gian cooldown, lấy key có thời gian cooldown sắp hết nhất
            earliest_key = min(self.keys, key=lambda k: self.key_status.get(k, {}).get("cooldown_until", 0.0))
            return earliest_key, self.current_index

    def mark_key_failure(self, key: str, is_rate_limit: bool = True):
        """Đánh dấu key bị lỗi để chuyển sang cooldown (ví dụ: 60 giây nếu 429)"""
        with self.lock:
            if key in self.key_status:
                self.key_status[key]["failures"] += 1
                cooldown_sec = 60.0 if is_rate_limit else 15.0
                self.key_status[key]["cooldown_until"] = time.time() + cooldown_sec
                mask = f"...{key[-6:]}" if len(key) > 6 else key
                print(f"[GeminiRotator] Key {mask} cooldown {cooldown_sec}s (rate_limit={is_rate_limit})")

    def mark_key_success(self, key: str):
        """Đặt lại số lần lỗi khi key hoạt động tốt"""
        with self.lock:
            if key in self.key_status:
                self.key_status[key]["failures"] = 0
                self.key_status[key]["cooldown_until"] = 0.0

    def generate_content(
        self,
        prompt: str,
        system_instruction: str = "",
        response_json: bool = False,
        temperature: float = 0.7,
        max_output_tokens: int = 4000
    ) -> Tuple[bool, str, Optional[str]]:
        """
        Gọi Gemini REST API với khả năng xoay vòng tự động qua toàn bộ danh sách key.
        Trả về: (success: bool, text_response: str, used_key_mask: Optional[str])
        """
        self.reload_keys()
        if not self.keys:
            return False, "Chưa cấu hình GEMINI_API_KEYS trong file .env", None

        # Thử qua tối đa số lượng keys trong danh sách
        attempts = len(self.keys)
        for attempt in range(attempts):
            key_info = self.get_available_key()
            if not key_info:
                break
            api_key, _ = key_info
            key_mask = f"...{api_key[-6:]}" if len(api_key) > 6 else api_key

            url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={api_key}"
            
            payload: Dict[str, Any] = {
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ],
                "generationConfig": {
                    "temperature": temperature,
                    "maxOutputTokens": max_output_tokens
                }
            }

            if system_instruction:
                payload["systemInstruction"] = {
                    "parts": [{"text": system_instruction}]
                }

            if response_json:
                payload["generationConfig"]["responseMimeType"] = "application/json"

            try:
                with httpx.Client(timeout=45.0) as client:
                    resp = client.post(url, json=payload)
                    
                    if resp.status_code == 200:
                        data = resp.json()
                        candidates = data.get("candidates", [])
                        if candidates:
                            parts = candidates[0].get("content", {}).get("parts", [])
                            if parts:
                                content_text = parts[0].get("text", "").strip()
                                self.mark_key_success(api_key)
                                return True, content_text, key_mask

                    elif resp.status_code in [429, 503]:
                        self.mark_key_failure(api_key, is_rate_limit=True)
                        print(f"[GeminiRotator] HTTP {resp.status_code} with key {key_mask}, switching to next key...")
                        continue
                    else:
                        print(f"[GeminiRotator] API Error {resp.status_code} on key {key_mask}: {resp.text[:100]}")
                        self.mark_key_failure(api_key, is_rate_limit=False)
                        continue

            except Exception as e:
                print(f"[GeminiRotator] Network error on key {key_mask}: {type(e).__name__}")
                self.mark_key_failure(api_key, is_rate_limit=False)
                continue

        return False, "Tất cả các Gemini API Key đều đang tạm thời bận hoặc hết hạn mức.", None

    def generate_json(
        self,
        prompt: str,
        system_instruction: str = "",
        max_output_tokens: int = 5000
    ) -> Tuple[bool, Any, Optional[str]]:
        """
        Gọi Gemini REST API với phản hồi JSON, tự động bóc tách markdown và parse JSON.
        """
        import re
        ok, text, key_mask = self.generate_content(
            prompt=prompt,
            system_instruction=system_instruction,
            response_json=True,
            max_output_tokens=max_output_tokens
        )
        if not ok:
            return False, None, key_mask

        try:
            clean_text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.MULTILINE)
            data = json.loads(clean_text)
            return True, data, key_mask
        except Exception as err:
            # Fallback: search first [ or {
            try:
                first_b = text.find('[')
                first_c = text.find('{')
                if first_b != -1 and (first_c == -1 or first_b < first_c):
                    last_b = text.rfind(']')
                    if last_b != -1:
                        data = json.loads(text[first_b:last_b+1])
                        return True, data, key_mask
                elif first_c != -1:
                    last_c = text.rfind('}')
                    if last_c != -1:
                        data = json.loads(text[first_c:last_c+1])
                        return True, data, key_mask
            except Exception:
                pass
            print(f"[GeminiRotator] JSON parsing error on key {key_mask}: {err}")
            return False, None, key_mask

# Singleton instance
gemini_rotator = GeminiKeyRotator()

