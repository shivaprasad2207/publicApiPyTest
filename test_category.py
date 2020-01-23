import pytest
import os
import re
import requests

test_conf = None
test_feature = None


@pytest.fixture
def execute_api(get_test_conf1):
    test_file = os.path.basename(__file__)
    file_name = test_file.replace(".py","")
    return get_test_conf1.get_test_config(file_name)


def test_t1 (execute_api):
    print (execute_api)