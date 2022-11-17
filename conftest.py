import pytest
import SRC.providers.jsonconfigprovider as jcp
import SRC.providers.osconfigprovider as ocp
from SRC.providers.providerconstants import CONF_PATH
from SRC.config import config
from SRC.models import usermodel

@pytest.fixture
def basic_types_data(scope='session'):
    c = config.Config([jcp.JSONConfigProvider(CONF_PATH), ocp.OSConfigProvider()])
    return c

@pytest.fixture
def user_model_fixture(basic_types_data):
    new_user = usermodel.UserModel(basic_types_data['user_fname'], basic_types_data['user_lname'])
    yield new_user
    del new_user
