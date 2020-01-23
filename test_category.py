import pytest
import os
import re
import requests
import logging

test_conf = None
test_feature = None


@pytest.fixture
def execute_api(get_test_conf):
    """
    :Algoritham:
        1. Get the current pytest filename.
        2. Get the the test config from fixture by inputting the current file name as
           it will include the information of feature the current pytest file will test.
        3. Create test url.
        4. perform get operation.
    :param get_test_conf:
    :return:
    """
    log = logging.getLogger('test_category::execute_api')
    global test_conf
    f_file_name = os.path.basename(__file__)
    test_conf = get_test_conf.get_test_config(f_file_name)
    url = test_conf["base_url"]
    global test_feature
    test_feature = re.match(r"test_(\w+).py", f_file_name).groups()
    feature = test_feature[0]
    test_url = test_conf[feature]['url']
    test_values = test_conf[feature]['value']
    f_url = url + test_url
    return {
        'url': f_url,
        'test_values': test_values
    }


def test_api_return_status(execute_api):
    """
    Test the api return status code
    """
    test_url = execute_api['url']
    test_values = execute_api['test_values']
    for value in test_values:
        url = test_url.replace('_fill_', value)
        ret = requests.get(url)
        ret_resp = ret.json()


def test_element_count(execute_api):
    """
       Test the api return of count of elements in the response.
    """
    pass