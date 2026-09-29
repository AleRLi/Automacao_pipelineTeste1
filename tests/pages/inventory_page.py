from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_PRODUCT_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart-']")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def add_product(self):
        self.click(*self.ADD_BACKPACK)

    def add_all_products(self):
        product_count = len(self.find_all(*self.ADD_PRODUCT_BUTTONS))
        for _ in range(product_count):
            self.click(*self.ADD_PRODUCT_BUTTONS)

    def go_to_cart(self):
        self.click(*self.CART)

    def get_cart_items_count(self):
        badges = self.find_all(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def logout(self):
        self.click(*self.MENU_BUTTON)
        self.click(*self.LOGOUT_LINK)

    def reset_app_state(self):
        self.click(*self.MENU_BUTTON)
        self.click(*self.RESET_LINK)

    def sort_by(self, value):
        Select(self.find(*self.SORT_DROPDOWN)).select_by_value(value)

    def get_product_prices(self):
        return [
            float(product.text.replace("$", ""))
            for product in self.find_all(*self.PRODUCT_PRICE)
        ]

    def get_product_names(self):
        return [product.text for product in self.find_all(*self.PRODUCT_NAME)]
