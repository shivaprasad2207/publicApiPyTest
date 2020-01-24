import pytest
import dispatcher
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope='module')
def get_test_conf():
    """
    Setup fixture will be used for all the pytest files within the this file folder.
    This setup method creates test dispatch object
    :return: TestDispatcher object
    """
    return dispatcher.TestDispatcher()
