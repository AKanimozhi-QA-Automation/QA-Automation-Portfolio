
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.selenium
def test_selenium_valid_login():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 15)

        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='username']")
            )
        ).send_keys("standard_user")

        driver.find_element(
            By.CSS_SELECTOR, "[data-test='password']"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.CSS_SELECTOR, "[data-test='login-button']"
        ).click()

        wait.until(EC.url_contains("inventory.html"))

        assert wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
            )
        ).is_displayed()

    finally:
        driver.quit()
