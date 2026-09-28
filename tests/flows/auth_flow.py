from tests.config.settings import BASE_URL
from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage


class AuthFlow:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)

    def login(self, user):
        self.login_page.open_login(BASE_URL)
        self.login_page.login(user.username, user.password)

    def logout(self):
        self.inventory_page.logout()
