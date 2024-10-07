import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import (
    forgot_password_page_url,
    login_page_url,
    test_user_login,
    test_user_password,
)

def test_login_via_forgot_password_button():
    driver = webdriver.Chrome()
    try:
        driver.get(forgot_password_page_url)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        assert "Проверьте свою почту" in driver.page_source  # Проверка сообщения об успешном запросе
        driver.get(login_page_url)  # Вернуться на страницу логина
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "Личный кабинет" in driver.page_source
    finally:
        driver.quit()