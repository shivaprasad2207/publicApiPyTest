import pytest
import os
import re
import requests
import logging

test_conf = None
test_feature = None


@pytest.fixture
def execute_api(get_test_conf):
    log = logging.getLogger('test_entries::execute_api')
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
    log = logging.getLogger('test_entries::test_api_return_status')
    ret_val = execute_api.status_code
    log.debug("Api Ret Value -- %s", ret_val)
    assert ret_val == 200


def test_element_count(execute_api):
    log = logging.getLogger('test_entries::test_element_count')
    api_response = execute_api.json()
    api_element_count = api_response['count']
    log.debug("Api Response element Count --  %s", api_element_count)
    resp_elements = len(api_response['entries'])
    assert api_element_count == resp_elements


def test_api_schema(execute_api):
    log = logging.getLogger('test_entries::test_api_schema')
    api_response = execute_api.json()
    api_schema = test_conf['entries']['schema']
    log.debug("Expected Api Schema %s", ' '.join(api_schema) )
    for entry in api_response['entries']:
        schema_resp_element = list(entry.keys())
        log.debug("Response: Api Schema %s -- ", ' '.join(schema_resp_element))
        assert schema_resp_element == api_schema


def test_api_schema_type_str(execute_api):
    log = logging.getLogger('test_entries::test_api_schema_type_str')
    api_response = execute_api.json()
    api_schema = test_conf['entries']['fields']["string"]
    log.debug("Expected Api String type columns -- %s", ' '.join(api_schema))
    for entry in api_response['entries']:
        for schema in api_schema:
            assert type(entry[schema]) is str


def test_api_schema_type_bool(execute_api):
    log = logging.getLogger('test_entries::test_api_schema_type_bool')
    api_response = execute_api.json()
    api_schema = test_conf['entries']['fields']["bool"]
    log.debug("Expected Api bool type columns -- %s", ' '.join(api_schema))
    for entry in api_response['entries']:
        for schema in api_schema:
            assert type(entry[schema]) is bool
