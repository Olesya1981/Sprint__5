from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver


class TestNavigation:

    def test_verify_click_navigation_personal_account(self, driver):
        # входим в аккаунт  пользователя с данными:
        driver.get(Urls.main_url)
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(PROFILE))
        profile = driver.find_element(*PROFILE).text
        assert profile == "Профиль"


    # Переход из личного кабинета в конструктор
    def test_navigation_from_personal_account_to_constructor(self, driver):
        # входим в аккаунт  пользователя с данными:
        driver.get(Urls.main_url)
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
        constructor_text = driver.find_element(*CONSTRUCT_BURGER).text
        assert constructor_text == 'Соберите бургер'


    def test_navigation_from_personal_account_to_logo_stellar_burgers(self, driver):
        driver.get(Urls.main_url)
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(LOGO_BUTTON))
        driver.find_element(*LOGO_BUTTON).click()
        check = driver.find_element(*CONSTRUCT_BURGER_XPATH).text
        assert check == 'Соберите бургер'

