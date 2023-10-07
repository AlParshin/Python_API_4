import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import requests

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def browser():
    service = Service(testdata['driver_path'])
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_token():
    response = requests.post(url=testdata['url'], data={
                             'username': testdata['username_api'], 'password': testdata['password_api']})
    return response.json()['token']
