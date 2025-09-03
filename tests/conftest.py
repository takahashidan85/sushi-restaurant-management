import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://127.0.0.1:5000/swagger"

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def expand_endpoint(driver, method: str, path: str):
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".opblock-tag"))
    )

    xpath = (
        f"//section[contains(@class,'opblock')][.//span[@class='opblock-summary-method' and text()='{method.upper()}'] "
        f"and .//span[@class='opblock-summary-path' and normalize-space(text())='{path}']]"
    )
    section = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", section)
    section.find_element(By.CSS_SELECTOR, ".opblock-summary").click()

    try_it = WebDriverWait(section, 30).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[contains(., 'Try it out')]"))
    )
    try_it.click()





"""def expand_endpoint(driver, method: str, path: str):
    locator = f"//span[text()='{method.upper()}']/ancestor::div[contains(., '{path}')]"
    endpoint = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, locator))
    )
    endpoint.click()
    try_it = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Try it out']"))
    )
    try_it.click()"""
