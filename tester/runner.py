# Test runner and QoS metrics
from tester.tests import run_tests


def calculate_p95(values):
    if not values:
        return 0

    values = sorted(values)
    index = int(0.95 * (len(values) - 1))
    return values[index]


def run_all_tests():
    tests = run_tests()

    passed = len([test for test in tests if test["status"] == "PASS"])
    failed = len([test for test in tests if test["status"] == "FAIL"])
    total = len(tests)

    latencies = [test["latency_ms"] for test in tests]
    latency_avg = round(sum(latencies) / len(latencies), 2) if latencies else 0
    latency_p95 = calculate_p95(latencies)

    error_rate = round(failed / total, 3) if total else 0

    return {
        "api": "ipify",
        "summary": {
            "passed": passed,
            "failed": failed,
            "total": total,
            "error_rate": error_rate,
            "latency_ms_avg": latency_avg,
            "latency_ms_p95": latency_p95
        },
        "tests": tests
    }
