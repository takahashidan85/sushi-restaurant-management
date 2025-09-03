from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import expand_endpoint

def test_sushiitem_update(driver):
    expand_endpoint(driver, "PUT", "/sushi-items/{id}")
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='name']")
    name_input.clear(); name_input.send_keys("Salmon Roll Updated")
    execute = driver.find_element(By.XPATH, "//button[text()='Execute']")
    execute.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Responses']"))
    )
    response = driver.find_element(By.XPATH, "//tr[@data-code='200']")
    assert response is not None
