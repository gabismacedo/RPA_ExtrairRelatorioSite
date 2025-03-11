from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# ESPERAR PARA ENCONTRAR O ELEMENTO
def wait_for_element(driver, element):
    try:
        wait = WebDriverWait(driver, 20)
        return wait.until(EC.element_to_be_clickable((By.XPATH, element)))
    except Exception:
        return False


def wait_for_element(driver, element, timer: float = 60):
    # Tentar encontrar o elemento por um tempo determinado, padronizado em 60s
    try:
        wait = WebDriverWait(driver, timer)
        return wait.until(EC.element_to_be_clickable((By.XPATH, element)))
    except Exception:
        return None