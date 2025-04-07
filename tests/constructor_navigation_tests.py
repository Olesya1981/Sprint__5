from locators import *
from baza import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.add_experimental_option("detach", True)
login, email, password = baza()

class TestConstructorNavigation:
    # Проверь, что работают переходы к разделам:
    def test_verify_navigation_in_constructor_elements_to_buns(self):
        driver.get(main_url)
        driver.implicitly_wait(2)
        driver.find_element(*SAUCES_CLICK).click()
        driver.implicitly_wait(2)
        driver.find_element(*BUNS_CLICK).click()
        buns = driver.find_element(*BUNS_CLASS).get_attribute('class')
        assert buns == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.quit()

    def test_verify_navigation_in_constructor_elements_to_sauces(self):
        driver.get(main_url)
        driver.implicitly_wait(2)
        driver.find_element(*SAUCES_CLICK).click()
        sauces = driver.find_element(*SAUCES_CLASS).get_attribute('class')
        assert sauces == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.quit()

    def test_verify_navigation_in_constructor_elements_to_toppings(self):
        driver.get(main_url)
        driver.implicitly_wait(2)
        driver.find_element(*TOPPINGS_CLICK).click()
        toppings = driver.find_element(*TOPPINGS_CLASS).get_attribute('class')
        assert toppings == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.quit()
