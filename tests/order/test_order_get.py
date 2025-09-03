from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import expand_endpoint

def test_order_get(driver):
    expand_endpoint(driver, "GET", "/orders/{id}")

    execute = driver.find_element(By.XPATH, "//button[text()='Execute']")
    execute.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Responses']"))
    )
    response = driver.find_element(By.XPATH, "//tr[@data-code='200']")
    assert response is not None
