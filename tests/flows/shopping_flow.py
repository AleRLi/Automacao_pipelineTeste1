from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from tests.pages.inventory_page import InventoryPage


class ShoppingFlow:
    def __init__(self, driver):
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    def add_backpack_and_open_cart(self):
        self.inventory_page.add_product()
        self.inventory_page.go_to_cart()

    def start_checkout_with_backpack(self):
        self.add_backpack_and_open_cart()
        self.cart_page.start_checkout()

    def complete_checkout(self, details):
        self.checkout_page.fill_form(
            details.first_name,
            details.last_name,
            details.postal_code,
        )
        self.checkout_page.continue_checkout()
        self.checkout_page.finish()
