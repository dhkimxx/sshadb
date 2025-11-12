import os
import pytest
from dotenv import load_dotenv

from sshadb import SSHAdb


load_dotenv()


@pytest.fixture(scope="session")
def client():
    host = os.getenv("SSHADB_HOST")
    print(host)
    user = os.getenv("SSHADB_USER")
    password = os.getenv("SSHADB_PASSWORD")
    key_path = os.getenv("SSHADB_KEY_PATH")
    try:
        port = int(os.getenv("SSHADB_PORT", "22"))
    except ValueError:
        port = 22
    try:
        timeout = float(os.getenv("SSHADB_TIMEOUT", "10"))
    except ValueError:
        timeout = 10.0

    if not host or not user:
        pytest.skip("Set SSHADB_HOST and SSHADB_USER to run integration tests")

    c = SSHAdb(
        host=host,
        user=user,
        port=port,
        password=password,
        key_path=key_path,
        timeout=timeout,
    )
    # 초기 연결/환경 검증: 원격에 접근 불가/타임아웃이면 전체 테스트 skip
    try:
        _ = c.devices()
    except Exception as e:
        pytest.skip(f"SSHADB connection check failed: {e}")
    yield c
    c.close()


@pytest.fixture(scope="session")
def test_serial():
    serial = os.getenv("SSHADB_SERIAL")
    if not serial:
        pytest.skip("Set SSHADB_SERIAL to run device-specific tests")
    return serial
