from tests.data.test_data import STANDARD_USER


def test_checkout_sem_preencher_dados(auth_flow, shopping_flow, driver):
    auth_flow.login(STANDARD_USER)
    shopping_flow.start_checkout_with_backpack()
    assert "checkout-step-one.html" in driver.current_url

    shopping_flow.checkout_page.continue_checkout()
    assert "First Name is required" in shopping_flow.checkout_page.get_error_message()


def test_checkout_parcial(auth_flow, shopping_flow):
    auth_flow.login(STANDARD_USER)
    shopping_flow.start_checkout_with_backpack()

    shopping_flow.checkout_page.fill_form(name="Alessandro")
    shopping_flow.checkout_page.continue_checkout()
    assert "Last Name is required" in shopping_flow.checkout_page.get_error_message()
