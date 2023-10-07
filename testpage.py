from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_INPUT_USERNAME = (
        By.XPATH, '''/html/body/div/main/div/div/div/form/div[1]/label/input''')
    LOCATOR_INPUT_PASSWORD = (
        By.XPATH, '''/html/body/div/main/div/div/div/form/div[2]/label/input''')
    LOCATOR_LOGIN_BUTTON = (
        By.XPATH, '''/html/body/div[1]/main/div/div/div/form/div[3]/button''')
    LOCATOR_CONTACT_BUTTON = (
        By.CSS_SELECTOR, '''#app > main > nav > ul > li:nth-child(2) > a''')
    LOCATOR_INPUT_NAME = (
        By.XPATH, '''/html/body/div[1]/main/div/div/form/div[1]/label/input''')
    LOCATOR_INPUT_EMAIL = (
        By.XPATH, '''/html/body/div[1]/main/div/div/form/div[2]/label/input''')
    LOCATOR_INPUT_CONTENT = (
        By.XPATH, '''/html/body/div[1]/main/div/div/form/div[3]/label/span/textarea''')
    LOCATOR_SEND_BUTTON = (
        By.XPATH, '''/html/body/div[1]/main/div/div/form/div[4]/button/div''')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_INPUT_USERNAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_password(self, word):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_INPUT_PASSWORD)
        login_field.clear()
        login_field.send_keys(word)

    def click_button(self):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_LOGIN_BUTTON)
        login_field.click()

    def click_contact(self):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_CONTACT_BUTTON)
        login_field.click()

    def enter_name(self, word):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_INPUT_NAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_email(self, word):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_INPUT_EMAIL)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_INPUT_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def send_contact(self):
        login_field = self.find_element(
            TestSearchLocators.LOCATOR_SEND_BUTTON)
        login_field.click()

    def switch(self):
        login_field = self.switch_to_alert()
        print(login_field.text)
