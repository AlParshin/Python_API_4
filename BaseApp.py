import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging

logging.basicConfig(level=logging.INFO, filename="Seminar_4.log", filemode="a",
                    encoding="UTF-8", format="%(asctime)s %(levelname)s %(message)s")

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']

    def find_element(self, locator, time=10):
        try:
            temp = WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(
                locator), message=f"Элемент {locator} не найден!")
            logging.info("Ok")
            return temp
        except:
            logging.error("GeekBrains")

    def get_element_property(self, mode, path, property):
        try:
            element = self.find_element(mode, path)
            temp = element.value_of_css_property(property)
            logging.info("Ok")
            return temp
        except:
            logging.error("GeekBrains")

    def go_to_site(self):
        try:
            temp = self.driver.get(self.base_url)
            logging.info("Ok")
            return temp
        except:
            logging.error("GeekBrains")

    def close(self):
        try:
            temp = self.driver.close()
            logging.info("Ok")
            return temp
        except:
            logging.error("GeekBrains")

    def switch_to_alert(self):
        try:
            temp = self.driver.switch_to.alert()
            logging.info("Ok")
            return temp
        except:
            logging.error("GeekBrains")
