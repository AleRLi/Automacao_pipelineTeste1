import pytest

from tests.config.settings import BASE_URL
from tests.data.test_data import INVALID_USER, LOCKED_OUT_USER, STANDARD_USER


def test_login_com_credenciais_validas(auth_flow, driver):
    auth_flow.login(STANDARD_USER)

    assert "inventory.html" in driver.current_url


def test_login_com_credenciais_invalidas(auth_flow):
    auth_flow.login(INVALID_USER)

    assert (
        "Username and password do not match" in auth_flow.login_page.get_error_message()
    )


def test_login_usuario_bloqueado(auth_flow):
    auth_flow.login(LOCKED_OUT_USER)

    assert (
        "Sorry, this user has been locked out"
        in auth_flow.login_page.get_error_message()
    )


@pytest.mark.parametrize(
    ("username", "password"),
    [
        (" standard_user", "secret_sauce"),
        ("standard_user", "secret_sauce "),
    ],
)
def test_login_com_espacamentos_nas_credenciais(auth_flow, username, password):
    auth_flow.login_page.open_login(BASE_URL)
    auth_flow.login_page.login(username, password)

    assert (
        "Username and password do not match" in auth_flow.login_page.get_error_message()
    )


def test_login_com_muitos_caracteres(auth_flow):
    auth_flow.login_page.open_login(BASE_URL)
    auth_flow.login_page.login("u" * 256, "p" * 256)

    assert (
        "Username and password do not match" in auth_flow.login_page.get_error_message()
    )


def test_login_com_senha_invalida(auth_flow):
    auth_flow.login_page.open_login(BASE_URL)
    auth_flow.login_page.login(STANDARD_USER.username, "senha_invalida")

    assert (
        "Username and password do not match" in auth_flow.login_page.get_error_message()
    )
