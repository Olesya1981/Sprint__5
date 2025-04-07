from locators import *
from baza import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.add_experimental_option("detach", True)
login, email, password = baza()


class TestLogout:
    # Проверь выход по кнопке «Выйти» в личном кабинете.
    def test_verify_logout_button_in_personal_account(self):
        # заходим в личный кабинет на главной
        driver.get(main_url)
        driver.find_element(*LOGIN_BUTTON).click()
        # driver.implicitly_wait()
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(registered_email)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(registered_password)
        driver.find_element(*LOGIN_LOGIN_BUTTON).click()
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        # кнопка выйти
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON))
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(ENTER_FORM))
        enter = driver.find_element(*ENTER_FORM).text
        assert enter == 'Вход'
        driver.quit()
