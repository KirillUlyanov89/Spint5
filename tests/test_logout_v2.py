import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data_v2 import (
    login_page_url,
    test_user_login,
    test_user_password,
)


class Locator:
    LOGOUT_BUTTON = "button[data-test='logout']"


def test_logout_from_personal_cabinet():
    driver = webdriver.Chrome()
    try:
        # Логин в систему
        driver.get(login_page_url)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        assert "Личный кабинет" in driver.page_source  # Проверка успешного входа

        # Выход из аккаунта
        driver.find_element(By.CSS_SELECTOR, Locator.LOGOUT_BUTTON).click()
        time.sleep(2)
        assert login_form.is_displayed()
    finally:
        driver.quit()