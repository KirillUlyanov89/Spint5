import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locator
from data import (
    register_page_url,
    test_user_name,
    test_user_login,
    test_user_password,
)

def test_successful_registration():
    driver = webdriver.Chrome()
    try:
        driver.get(register_page_url)  # Переброс на страницу регистрации

        # Вводим данные для регистрации
        driver.find_element(By.CSS_SELECTOR, Locator.NAME_FIELD).send_keys(test_user_name)
        driver.find_element(By.CSS_SELECTOR, Locator.EMAIL_FIELD).send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, Locator.PASSWORD_FIELD).send_keys(test_user_password)

        driver.find_element(By.CSS_SELECTOR, Locator.REGISTER_BUTTON).click()


        time.sleep(2)  # Ожидание
        assert login_button.is_displayed()
    finally:
        driver.quit()
 #
def test_failed_registration_short_password():
    driver = webdriver.Chrome()
    try:
        driver.get(register_page_url)

        driver.find_element(By.CSS_SELECTOR, Locator.NAME_FIELD).send_keys(test_user_name)
        driver.find_element(By.CSS_SELECTOR, Locator.EMAIL_FIELD).send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, Locator.PASSWORD_FIELD).send_keys("555")  # Корректный тест на короткий пароль

        driver.find_element(By.CSS_SELECTOR, Locator.REGISTER_BUTTON).click()

        # Проверка ошибки для некорректного пароля
        time.sleep(2)
        assert password_error_message.is_displayed()
    finally:
        driver.quit()
