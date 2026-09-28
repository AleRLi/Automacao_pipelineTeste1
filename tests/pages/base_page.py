from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.config.settings import WAIT_TIMEOUT_SECONDS


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return WebDriverWait(self.driver, WAIT_TIMEOUT_SECONDS).until(
            EC.presence_of_element_located((by, value))
        )

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        element = WebDriverWait(self.driver, WAIT_TIMEOUT_SECONDS).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def type(self, by, value, text):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text

    def is_displayed(self, by, value):
        return self.find(by, value).is_displayed()
