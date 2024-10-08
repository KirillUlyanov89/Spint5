import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import (
    main_page_url,
    test_user_login,
    test_user_password,
)
#
class Locator:
    CONSTRUCTOR_BUTTON = "button[data-test='constructor']"
    BUNS_SECTION = "a[data-test='buns']"
    SAUCES_SECTION = "a[data-test='sauces']"
    FILLINGS_SECTION = "a[data-test='fillings']"

def test_navigate_to_constructor():
    driver = webdriver.Chrome()
    try:
        driver.get(main_page_url)
        driver.find_element(By.CSS_SELECTOR, "button[data-test='login-main']").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Переход на страницу конструктора
        driver.find_element(By.CSS_SELECTOR, Locator.CONSTRUCTOR_BUTTON).click()
        assert "Конструктор" in driver.page_source  # Проверка, что находимся в конструкторе
    finally:
        driver.quit()

def test_navigate_to_sections():
    driver = webdriver.Chrome()
    try:
        driver.get(main_page_url)
        driver.find_element(By.CSS_SELECTOR, "button[data-test='login-main']").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(test_user_login)
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(test_user_password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Проверка переходов между разделами
        driver.find_element(By.CSS_SELECTOR, Locator.BUNS_SECTION).click()
        time.sleep(2)
        assert "Булки" in driver.page_source  # Проверка находимся в разделе "Булки"

        driver.find_element(By.CSS_SELECTOR, Locator.SAUCES_SECTION).click()
        time.sleep(2)
        assert "Соусы" in driver.page_source  # Проверка находимся в разделе "Соусы"

        driver.find_element(By.CSS_SELECTOR, Locator.FILLINGS_SECTION).click()
        time.sleep(2)
        assert "Начинки" in driver.page_source  # Проверка находимся в разделе "Начинки"
    finally:
        driver.quit()