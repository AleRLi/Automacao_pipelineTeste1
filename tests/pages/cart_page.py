from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def cart_is_empty(self):
        return len(self.find_all(*self.CART_ITEMS)) == 0