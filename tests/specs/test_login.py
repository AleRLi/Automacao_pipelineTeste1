from tests.data.test_data import INVALID_USER, LOCKED_OUT_USER


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
