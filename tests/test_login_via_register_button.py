import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import (
    main_page_url,
    test_user_login,
    test_user_password,
)

class Locator:
    LOGIN_BUTTON_REGISTER = "button[data-test='login-register']"

def test_login_via_register_button():
    driver = webdriver.Chrome()
    try:
        driver.get(main_page_url)
        driver.find_element(By.CSS_SELECTOR, Locator.LOGIN_BUTTON_REGISTER).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "Личный кабинет" in driver.page_source
    finally:
        driver.quit()