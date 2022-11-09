import pytest
from os import environ
import SRC.providers.jsonconfigprovider as jcp
import SRC.providers.osconfigprovider as ocp
from SRC.providers.providerconstants import CONF_PATH
from SRC.config import config

@pytest.fixture
def basic_types_data(scope='session'):
    environ['test_data'] = "OS TEST DATA"
    
    c = config.Config([jcp.JSONConfigProvider(CONF_PATH), ocp.OSConfigProvider()])
    return c
