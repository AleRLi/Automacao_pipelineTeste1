from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def fill_form(self, name=None, last=None, zip_code=None):
        if name is not None:
            self.type(*self.FIRST_NAME, name)
        if last is not None:
            self.type(*self.LAST_NAME, last)
        if zip_code is not None:
            self.type(*self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.click(*self.CONTINUE)

    def finish(self):
        self.click(*self.FINISH)

    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MSG)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)
