from tests.data.test_data import CHECKOUT_DETAILS, STANDARD_USER


def test_compra_produto_com_sucesso(auth_flow, shopping_flow, driver):
    auth_flow.login(STANDARD_USER)
    assert "inventory.html" in driver.current_url

    shopping_flow.start_checkout_with_backpack()
    assert "checkout-step-one.html" in driver.current_url

    shopping_flow.complete_checkout(CHECKOUT_DETAILS)
    assert "Thank you" in shopping_flow.checkout_page.get_success_message()
