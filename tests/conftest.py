import pytest

from tests.fixtures.driver import driver as _driver  # noqa: F401
from tests.flows.auth_flow import AuthFlow
from tests.flows.shopping_flow import ShoppingFlow


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: critical end-to-end scenarios")


@pytest.fixture
def auth_flow(driver):
    return AuthFlow(driver)


@pytest.fixture
def shopping_flow(driver):
    return ShoppingFlow(driver)
