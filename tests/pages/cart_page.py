from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove-']")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def cart_is_empty(self):
        return len(self.find_all(*self.CART_ITEMS)) == 0

    def get_cart_items_count(self):
        return len(self.find_all(*self.CART_ITEMS))

    def remove_first_item(self):
        self.click(*self.REMOVE_BUTTONS)
