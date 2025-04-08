from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_main_page_login_button_authorisation(self, driver):  #
        driver.get(Urls.main_url)
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(PROFILE))
        profile = driver.find_element(*PROFILE).text
        assert profile == "Профиль"


    # вход через кнопку «Личный кабинет»,
    def test_personal_account_button_authorisation(self, driver):  #
        driver.get(Urls.main_url)
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(PROFILE))
        profile = driver.find_element(*PROFILE).text
        assert profile == "Профиль"

    # вход через кнопку в форме регистрации,
    def test_login_button_in_registration_form_authorisation(self, driver):
        driver.get(Urls.registration_url)
        driver.find_element(*ENTER_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(PROFILE))
        profile = driver.find_element(*PROFILE).text
        assert profile == "Профиль"


    # вход через кнопку в форме восстановления пароля.
    def test_login_button_in_forgot_password_form_authorisation(self, driver):
        driver.get(Urls.forgot_password_url)
        driver.find_element(*REMEMBER_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(PROFILE))
        profile = driver.find_element(*PROFILE).text
        assert profile == "Профиль"
