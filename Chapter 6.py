def to_secs(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds


def test_suite():
    test_suite(to_secs(2, 30, 10) == 9010)
    test_suite(to_secs(2, 0, 0) == 7200)
    test_suite(to_secs(0, 2, 0) == 120)
    test_suite(to_secs(0, 0, 42) == 42)
    test_suite(to_secs(0, -10, 10) == -590)

print("All tests passed")
