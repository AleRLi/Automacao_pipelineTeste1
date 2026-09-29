import time

from selenium.webdriver.common.by import By

# =========================================================
# CENÁRIO - CONTINUAR COMPRANDO APÓS ADICIONAR ITEM
# =========================================================


def test_continuar_comprando_apos_adicionar_item(driver):

    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # =========================
    # 2. ADICIONAR ITEM AO CARRINHO
    # =========================
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    # =========================
    # 3. ACESSAR O CARRINHO
    # =========================
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Validação de que está no carrinho
    assert "cart.html" in driver.current_url

    # =========================
    # 4. VOLTAR PARA LISTA DE PRODUTOS
    # =========================
    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(3)

    # =========================
    # 5. VALIDAR LISTA DE PRODUTOS
    # =========================
    assert "inventory.html" in driver.current_url

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(produtos) > 0

    time.sleep(2)
