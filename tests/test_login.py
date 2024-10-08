import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import (
    main_page_url,
    login_page_url,
    test_user_login,
    test_user_password,
)

class Locator:
    LOGIN_BUTTON_MAIN = "button[data-test='login-main']"
    LOGIN_BUTTON_PROFILE = "button[data-test='login-cabinet']"
    LOGIN_BUTTON_REGISTER = "button[data-test='login-register']"
    LOGIN_BUTTON_RECOVERY = "button[data-test='login-recovery']"

def test_login_via_main_page():
    driver = webdriver.Chrome()
    try:
        driver.get(main_page_url)
        driver.find_element(By.CSS_SELECTOR, Locator.LOGIN_BUTTON_MAIN).click()
        time.sleep(2)  # Ожидание загрузки страницы
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "Личный кабинет" in driver.page_source  # Проверка успешного входа
    finally:
        driver.quit()

def test_login_via_profile_button():
    driver = webdriver.Chrome()
    try:
        driver.get(main_page_url)
        driver.find_element(By.CSS_SELECTOR, Locator.LOGIN_BUTTON_PROFILE).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "Личный кабинет" in driver.page_source
    finally:
        driver.quit()

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