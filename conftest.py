import pytest
import json


def pytest_addoption(parser):
    parser.addoption("--test_config", action="store")


@pytest.fixture(scope='module')
def get_test_conf(pytestconfig):
    test_config_file = pytestconfig.getoption("--test_config").lower()
    with open(test_config_file) as f:
        test_config = json.load(f)
    return test_config
