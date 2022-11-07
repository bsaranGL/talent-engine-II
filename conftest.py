import pytest
from SRC.config import config, configprovider

c = config.Config([configprovider.JsonConfigProvider(), configprovider.OsConfigProvider()])

@pytest.fixture
def provide_string():
    return c.get("myvar")

@pytest.fixture
def provide_int():
    return c.get("int_data")

@pytest.fixture
def provide_float():
    return c.get("float_data")