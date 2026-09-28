from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pytest
import tempfile
import os
 
@pytest.fixture
def driver():
    chrome_options = Options()
    
    # Verifica se deve rodar em modo headless (ex: via variável de ambiente no CI)
    # Você pode definir HEADLESS=true no GitHub Actions se desejar
    is_ci = os.getenv("CI", "false").lower() == "true"
    if is_ci or os.getenv("HEADLESS", "false").lower() == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    # Perfil limpo e isolado (Corrigido para --user-data-dir)
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
     
    # Desativa Password Manager convencional
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        # DESATIVA DETECÇÃO DE VAZAMENTO
        "profile.password_manager_leak_detection": False
    }
     
    chrome_options.add_experimental_option("prefs", prefs)
     
    # Desativa Safe Browsing (remove alertas de segurança)
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--safebrowsing-disable-leakdetection")
     
    # Hardening adicional
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")

    # Inicialização do driver compatível com WebDriver Manager e ambientes de CI
    if is_ci:
        # No Linux do GitHub Actions, o Chrome já é instalado via apt-get no workflow
        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Localmente no Windows, gerencia o driver automaticamente
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()

    yield driver

    driver.quit()