import pytest

def test_str_t(basic_types_data):
    assert type(basic_types_data['str_data']) == str

@pytest.mark.xfail
def test_str_f(basic_types_data):
    assert type(basic_types_data['str_data']) == int
    
def test_int_t(basic_types_data):
    assert type(basic_types_data['int_data']) == int

@pytest.mark.xfail
def test_int_f(basic_types_data):
    assert type(basic_types_data['int_data']) == float
    
def test_float_t(basic_types_data):
    assert type(basic_types_data['float_data']) == float

@pytest.mark.xfail
def test_float_f(basic_types_data):
    assert type(basic_types_data['float_data']) == str
    
def test_list_t(basic_types_data):
    assert type(basic_types_data['list_data']) == list

@pytest.mark.xfail
def test_list_f(basic_types_data):
    assert type(basic_types_data['list_data']) == int
    
def test_tuple_t(basic_types_data):
    t = tuple(basic_types_data['tuple_data'])
    assert type(t) == tuple

@pytest.mark.xfail
def test_tuple_f(basic_types_data):
    t = tuple(basic_types_data['tuple_data'])
    assert type(t) == int

def test_dict_t(basic_types_data):
    assert type(basic_types_data['dict_data']) == dict

@pytest.mark.xfail
def test_dict_f(basic_types_data):
    assert type(basic_types_data['dict_data']) == int
    
def test_set_t(basic_types_data):
    s = set(basic_types_data['set_data'])
    assert type(s) == set

@pytest.mark.xfail
def test_set_f(basic_types_data):
    s = set(basic_types_data['set_data'])
    assert type(s) == str
    
def test_env_var_t(basic_types_data):
    assert basic_types_data['test_data'] == "OS TEST DATA"

@pytest.mark.xfail    
def test_env_var_f(basic_types_data):
    assert basic_types_data['test_data'] == "Hello"
    
def test_user_t(user_model_fixture):
    assert user_model_fixture.get_login() == "bsaran"
    
@pytest.mark.xfail
def test_user_f(user_model_fixture):
    assert user_model_fixture.get_login() == "jdoe"