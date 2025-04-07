from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import *
from conftest import driver

login, email, password = baza()


class TestRegistration:
    # регистрация и вход
    def test_registration_with_valid_name_email_password_is_successful(self, driver):
        driver.get(Urls.login_url)
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME_FIELD).send_keys(login)
        driver.find_element(*REGISTRATION_EMAIL_BUTTON).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD_BUTTON).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON_FINAL).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(ENTER_FORM))
        assert driver.find_element(*ENTER_FORM).text == 'Вход', \
            "Форма регистрации работает с ошибкой"
        driver.quit()

    # регистрация с некорректным паролем
    def test_invalid_password_error(self, driver):
        error_message = 'Некорректный пароль'
        driver.get(Urls.login_url)
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME_FIELD).send_keys(login)
        driver.find_element(*REGISTRATION_EMAIL_BUTTON).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD_BUTTON).send_keys(incorrect_password)
        driver.find_element(*REGISTRATION_BUTTON_FINAL).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(INVALID_PASSWORD_ERROR))
        assert driver.find_element(*INVALID_PASSWORD_ERROR).text == error_message
        driver.quit()
