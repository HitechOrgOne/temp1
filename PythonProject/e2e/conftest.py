import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://example.com",
        help="Base URL for the application under test",
    )

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("base_url")
