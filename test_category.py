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
    status = test_conf[feature]['status']
    parent = test_conf[feature]['parent']
    f_url = url + test_url
    return {
        'url': f_url,
        'test_values': test_values,
        'status': status,
        'parent': parent
    }


def test_api_return_status(execute_api):
    """
    Test the api return status code
    """
    log = logging.getLogger('test_category::execute_api')
    test_url = execute_api['url']
    test_values = execute_api['test_values']
    resp_state = int(execute_api['status'])
    for value in test_values:
        url = test_url.replace('_fill_', value)
        log.debug("Api to Test -- %s", url)
        ret = requests.get(url)
        ret_resp = ret.status_code
        log.debug("Api Ret Value -- %s", ret_resp)
        assert ret_resp == resp_state


def test_element_count(execute_api):
    """
       Test the api return of count of elements in the response.
    """
    log = logging.getLogger('test_category::execute_api')
    test_url = execute_api['url']
    test_values = execute_api['test_values']
    for value in test_values:
        url = test_url.replace('_fill_', value)
        log.debug("Api to Test -- %s", url)
        ret = requests.get(url)
        api_response = ret.json()
        api_element_count = api_response['count']
        log.debug("Api Response element Count --  %s", api_element_count)
        resp_elements = len(api_response['entries'])
        assert api_element_count == resp_elements


def test_element_with_data(execute_api):
    """
       Test the api return of elements with correct data in the response.
    """
    log = logging.getLogger('test_category::execute_api')
    test_url = execute_api['url']
    test_values = execute_api['test_values']
    parent = execute_api['parent']
    for value in test_values:
        url = test_url.replace('_fill_', value)
        log.debug("Api to Test -- %s", url)
        ret = requests.get(url)
        api_response = ret.json()
        api_elements = api_response[parent]
        for element in api_elements:
            element_data = element['Category']
            log.debug("Api Response element data --  %s", element_data)
            log.debug("Expected data --  %s", value)
            assert element_data == value
