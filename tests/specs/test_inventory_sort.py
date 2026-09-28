from tests.data.test_data import STANDARD_USER


def test_ordenar_produtos_por_preco_crescente(auth_flow, shopping_flow):
    auth_flow.login(STANDARD_USER)
    inventory_page = shopping_flow.inventory_page
    inventory_page.sort_by("lohi")

    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices)


def test_ordenar_produtos_por_nome(auth_flow, shopping_flow):
    auth_flow.login(STANDARD_USER)
    inventory_page = shopping_flow.inventory_page
    inventory_page.sort_by("az")

    names = inventory_page.get_product_names()
    assert names == sorted(names)
