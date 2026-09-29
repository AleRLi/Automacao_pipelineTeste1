import pytest

from tests.data.test_data import CHECKOUT_DETAILS, STANDARD_USER


def test_compra_produto_com_sucesso(auth_flow, shopping_flow, driver):
    auth_flow.login(STANDARD_USER)
    assert "inventory.html" in driver.current_url

    shopping_flow.start_checkout_with_backpack()
    assert "checkout-step-one.html" in driver.current_url

    shopping_flow.complete_checkout(CHECKOUT_DETAILS)
    assert "Thank you" in shopping_flow.checkout_page.get_success_message()


def test_compra_de_todos_os_produtos(auth_flow, shopping_flow, driver):
    auth_flow.login(STANDARD_USER)
    shopping_flow.inventory_page.add_all_products()

    assert shopping_flow.inventory_page.get_cart_items_count() == 6
    shopping_flow.inventory_page.go_to_cart()
    assert shopping_flow.cart_page.get_cart_items_count() == 6

    shopping_flow.cart_page.start_checkout()
    assert "checkout-step-one.html" in driver.current_url
    shopping_flow.complete_checkout(CHECKOUT_DETAILS)

    assert "Thank you" in shopping_flow.checkout_page.get_success_message()


@pytest.mark.xfail(
    reason="Swag Labs permite iniciar o checkout com o carrinho vazio",
)
def test_nao_deve_iniciar_compra_sem_itens(auth_flow, shopping_flow, driver):
    auth_flow.login(STANDARD_USER)
    shopping_flow.inventory_page.go_to_cart()
    assert shopping_flow.cart_page.cart_is_empty()

    shopping_flow.cart_page.start_checkout()

    assert "cart.html" in driver.current_url
