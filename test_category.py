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
    test_url = test_conf[test_feature[0]]['url']
    f_url = url + test_url
    log.debug("Url to Test %s", f_url)
    return requests.get(f_url)


def test_api_return_status(execute_api):
    """
    Test the api return status code
    """
    log = logging.getLogger('test_category::test_api_return_status')
    ret_val = execute_api.status_code
    log.debug("Api Ret Value -- %s", ret_val)
    assert ret_val == 200


def test_element_count(execute_api):
    """
       Test the api return of count of elements in the response.
    """
    log = logging.getLogger('test_category::test_element_count')
    api_response = execute_api.json()
    api_element_count = api_response['count']
    log.debug("Api Response element Count --  %s", api_element_count)
    resp_elements = len(api_response['entries'])
    assert api_element_count == resp_elements

