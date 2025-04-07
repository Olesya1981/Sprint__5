import pytest
from locators import *
from baza import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.add_experimental_option("detach", True)
login, email, password = baza()


class TestRegistration:
    # регистрация и вход
    def test_registration_with_valid_name_email_password_is_successful(self):
        driver.get(login_url)
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME_FIELD).send_keys(login)
        driver.find_element(*REGISTRATION_EMAIL_BUTTON).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD_BUTTON).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON_FINAL).click()
        driver.implicitly_wait(2)
        assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/h2[text() = 'Вход']").text == 'Вход', \
            "Форма регистрации работает с ошибкой"
        driver.quit()

    # регистрация с некорректным паролем
    def test_invalid_password_error(self):
        error_message = 'Некорректный пароль'
        driver.get(login_url)
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_NAME_FIELD).send_keys(login)
        driver.find_element(*REGISTRATION_EMAIL_BUTTON).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD_BUTTON).send_keys(incorrect_password)
        driver.find_element(*REGISTRATION_BUTTON_FINAL).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(INVALID_PASSWORD_ERROR))
        assert driver.find_element(*INVALID_PASSWORD_ERROR).text == error_message
        driver.quit()
