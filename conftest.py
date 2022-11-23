import pytest
import src.providers.jsonconfigprovider as jcp
import src.providers.osconfigprovider as ocp
from src.providers.providerconstants import CONF_PATH
from src.config import config
from src.models import usermodel

@pytest.fixture
def basic_types_data(scope='session'):
    c = config.Config([jcp.JSONConfigProvider(CONF_PATH), ocp.OSConfigProvider()])
    return c

@pytest.fixture
def user_model_fixture(basic_types_data):
    new_user = usermodel.UserModel(basic_types_data['user_fname'], basic_types_data['user_lname'])
    yield new_user
    del new_user
