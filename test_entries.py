import pytest
import os
import re
import requests

test_conf = None
test_feature = None


@pytest.fixture
def execute_api(get_test_conf):
    url = get_test_conf["base_url"]
    global test_conf
    test_conf = get_test_conf
    file_name = os.path.basename(__file__)
    global test_feature
    test_feature = re.match(r"test_(\w+).py", file_name).groups()
    test_url = get_test_conf[test_feature[0]]['url']
    return requests.get(url + test_url)


def test_api_return_status(execute_api):
    assert execute_api.status_code == 200, "api return code as expected"


def test_element_count(execute_api):
    api_response = execute_api.json()
    api_element_count = api_response['count']
    resp_elements = len(api_response['entries'])
    assert api_element_count == resp_elements, "response has expected element entries"


def test_api_schema(execute_api):
    api_response = execute_api.json()
    api_schema = test_conf['entries']['schema']
    for entry in api_response['entries']:
        schema_resp_element = list(entry.keys())
        assert schema_resp_element == api_schema, "response entries element schema is as expected"
