from tests.data.test_data import STANDARD_USER


def test_logout_com_sucesso(auth_flow):
    auth_flow.login(STANDARD_USER)
    auth_flow.logout()

    assert auth_flow.login_page.is_login_form_visible()
