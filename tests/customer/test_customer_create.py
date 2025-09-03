from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import expand_endpoint

def test_customer_create(driver):
    print(driver.page_source[:2000])
    expand_endpoint(driver, "POST", "/customers")
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='name']")
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='email']")
    name_input.clear(); email_input.clear()
    name_input.send_keys("Alice")
    email_input.send_keys("alice@example.com")
    execute = driver.find_element(By.XPATH, "//button[text()='Execute']")
    execute.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Responses']"))
    )
    response = driver.find_element(By.XPATH, "//tr[@data-code='201']")
    assert response is not None
