# HTTP client for API tests
import time
import requests

BASE_URL = "https://api.ipify.org"


def call_ipify(format_type="json"):
    url = f"{BASE_URL}?format={format_type}"

    for attempt in range(2):  # 1 essai + 1 retry max
        try:
            start = time.time()
            response = requests.get(url, timeout=3)
            latency_ms = round((time.time() - start) * 1000, 2)

            content_type = response.headers.get("Content-Type", "")

            return {
                "status_code": response.status_code,
                "content_type": content_type,
                "body": response.text,
                "json": response.json() if "json" in content_type else None,
                "latency_ms": latency_ms,
                "error": None
            }

        except requests.exceptions.RequestException as e:
            if attempt == 1:
                return {
                    "status_code": 500,
                    "content_type": "",
                    "body": "",
                    "json": None,
                    "latency_ms": 0,
                    "error": str(e)
                }
