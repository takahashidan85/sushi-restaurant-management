from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import expand_endpoint

def test_orderdetail_create(driver):
    expand_endpoint(driver, "POST", "/order-details")
    oid_input = driver.find_element(By.XPATH, "//input[@placeholder='order_id']")
    sid_input = driver.find_element(By.XPATH, "//input[@placeholder='sushi_item_id']")
    qty_input = driver.find_element(By.XPATH, "//input[@placeholder='quantity']")
    oid_input.clear(); sid_input.clear(); qty_input.clear()
    oid_input.send_keys("1")
    sid_input.send_keys("1")
    qty_input.send_keys("2")
    execute = driver.find_element(By.XPATH, "//button[text()='Execute']")
    execute.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Responses']"))
    )
    response = driver.find_element(By.XPATH, "//tr[@data-code='201']")
    assert response is not None
