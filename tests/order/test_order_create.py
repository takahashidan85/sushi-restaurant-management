from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import expand_endpoint

def test_order_create(driver):
    expand_endpoint(driver, "POST", "/orders")
    cid_input = driver.find_element(By.XPATH, "//input[@placeholder='customer_id']")
    otype_input = driver.find_element(By.XPATH, "//input[@placeholder='order_type']")
    cid_input.clear(); otype_input.clear()
    cid_input.send_keys("1")
    otype_input.send_keys("dine-in")
    execute = driver.find_element(By.XPATH, "//button[text()='Execute']")
    execute.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Responses']"))
    )
    response = driver.find_element(By.XPATH, "//tr[@data-code='201']")
    assert response is not None
