import yaml
import pytest
from REST_API import *
from testpage import OperationsHelper

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_web_simple(browser):
    value = OperationsHelper(browser)
    value.go_to_site()
    value.enter_login(testdata['user'])
    value.enter_password(testdata['password'])
    value.click_button()
    value.click_contact()
    value.enter_name('a')
    value.enter_email('a@a')
    value.enter_content('aaa')
    value.send_contact()
    value.switch()
    assert True


pytest.fixture()


def test_api_step_1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 80657 in lst_id


pytest.fixture()


def test_api_step_2(get_token):
    create_post(get_token)
    result = get_by_description(get_token)
    print(result)
    lst = result['data']
    lst_id = [el["description"] for el in lst]
    assert 'desc45678' in lst_id


if __name__ == '__main__':
    pytest.main(['-v'])
