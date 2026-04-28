# API contract tests
import re
from tester.client import call_ipify


def run_tests():
    results = []

    response = call_ipify("json")
    ip_value = response["json"].get("ip") if response["json"] else None

    tests = [
        ("Status HTTP 200", response["status_code"] == 200),
        ("Content-Type JSON", "json" in response["content_type"]),
        ("Champ ip présent", ip_value is not None),
        ("Type du champ ip = string", isinstance(ip_value, str)),
        ("Format IPv4 valide", bool(re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_value or ""))),
        ("Latence inférieure à 3000 ms", response["latency_ms"] < 3000),
    ]

    for name, passed in tests:
        results.append({
            "name": name,
            "status": "PASS" if passed else "FAIL",
            "latency_ms": response["latency_ms"],
            "details": "" if passed else "Test échoué"
        })

    return results
