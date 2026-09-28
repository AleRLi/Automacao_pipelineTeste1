import os


BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com").rstrip("/")
WAIT_TIMEOUT_SECONDS = float(os.getenv("WAIT_TIMEOUT_SECONDS", "10"))
