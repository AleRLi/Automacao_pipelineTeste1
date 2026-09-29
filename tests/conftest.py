import pytest

from tests.flows.auth_flow import AuthFlow
from tests.flows.shopping_flow import ShoppingFlow

pytest_plugins = ("tests.fixtures.driver",)


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: critical end-to-end scenarios")


@pytest.fixture
def auth_flow(driver):
    return AuthFlow(driver)


@pytest.fixture
def shopping_flow(driver):
    return ShoppingFlow(driver)
