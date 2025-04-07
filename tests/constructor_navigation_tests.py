from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver


class TestConstructorNavigation:
    # Проверь, что работают переходы к разделам:
    def test_verify_navigation_in_constructor_elements_to_buns(self, driver):
        driver.get(Urls.main_url)
        driver.find_element(*SAUCES_CLICK).click()
        driver.find_element(*BUNS_CLICK).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(BUNS_CLASS))
        buns = driver.find_element(*BUNS_CLASS).get_attribute('class')
        assert buns == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.quit()

    def test_verify_navigation_in_constructor_elements_to_sauces(self, driver):
        driver.get(Urls.main_url)
        driver.find_element(*SAUCES_CLICK).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(SAUCES_CLASS))
        sauces = driver.find_element(*SAUCES_CLASS).get_attribute('class')
        assert sauces == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.quit()

    def test_verify_navigation_in_constructor_elements_to_toppings(self, driver):
        driver.get(Urls.main_url)
        driver.find_element(*TOPPINGS_CLICK).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(TOPPINGS_CLASS))
        toppings = driver.find_element(*TOPPINGS_CLASS).get_attribute('class')
        assert toppings == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        driver.quit()
