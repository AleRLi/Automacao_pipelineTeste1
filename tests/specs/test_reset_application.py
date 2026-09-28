from tests.data.test_data import STANDARD_USER


def test_resetar_carrinho(auth_flow, shopping_flow):
    auth_flow.login(STANDARD_USER)
    inventory_page = shopping_flow.inventory_page
    inventory_page.add_product()
    assert inventory_page.get_cart_items_count() == 1

    inventory_page.reset_app_state()
    assert inventory_page.get_cart_items_count() == 0
