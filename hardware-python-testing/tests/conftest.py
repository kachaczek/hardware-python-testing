import pytest

@pytest.fixture(scope="session", autouse=True)
def banner():
    print("\n=== Running hardware tests ===\n")