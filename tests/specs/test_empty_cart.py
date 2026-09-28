from tests.data.test_data import STANDARD_USER


def test_acessar_carrinho_sem_itens(auth_flow, shopping_flow, driver):
    auth_flow.login(STANDARD_USER)
    shopping_flow.inventory_page.go_to_cart()

    assert "cart.html" in driver.current_url
    assert shopping_flow.cart_page.cart_is_empty()
