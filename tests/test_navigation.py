import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import (
    main_page_url,
    login_page_url,
    profile_page_url,
    test_user_login,
    test_user_password,
)

class Locator:
    PERSONAL_CABINET_BUTTON = "a[data-test='personal-cabinet']"

def test_navigate_to_personal_cabinet():
    driver = webdriver.Chrome()
    try:
        driver.get(main_page_url)
        driver.find_element(By.CSS_SELECTOR, "button[data-test='login-main']").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        driver.find_element(By.CSS_SELECTOR, Locator.PERSONAL_CABINET_BUTTON).click()
        assert "Личный кабинет" in driver.page_source  # Проверка перехода
    finally:
        driver.quit()