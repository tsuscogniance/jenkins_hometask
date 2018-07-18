import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from locators import Locators


class TestMeestLogistics(object):
    @classmethod
    def setup_class(cls):
        cls.shipping_type_list = ['Select shipping type', 'Home delivery', 'Branch']
        cls.chrome = webdriver.Chrome()
        cls.chrome.get("https://my.meest.us/en")
        cls.chrome.implicitly_wait(10)

    def test_empty_form_submit(self):
        self.__return__visible__element__(By.LINK_TEXT, Locators.calculation_link).click()
        sleep(2)  # wait for scrolling page down
        submit_button = self.chrome.find_element_by_css_selector(Locators.submit_form_button)
        submit_button.click()
        empty_country_field = self.chrome.find_element_by_css_selector(Locators.country_empty_field).text
        empty_shipping_method = self.chrome.find_element_by_css_selector(Locators.shipping_empty_method).text
        empty_weight_field = self.chrome.find_element_by_css_selector(Locators.weight_empty_field).text
        shipping_cost = self.chrome.find_element_by_css_selector(Locators.shipping_cost).text
        total_cost = self.chrome.find_element_by_css_selector(Locators.total_cost).text

        assert empty_country_field == 'This field can’t be blank'
        assert empty_shipping_method == 'This field can’t be blank'
        assert empty_weight_field == 'This field can’t be blank'
        assert shipping_cost == '$ 0.00'
        assert total_cost == '$ 0.00'
        assert submit_button.is_enabled()

    def test_check_dropdowns(self):
        self.__return__visible__element__(By.LINK_TEXT, Locators.calculation_link).click()
        sleep(2)  # wait for scrolling page down

        countries_dropdown = self.chrome.find_element_by_css_selector(Locators.select_country)
        Select(countries_dropdown).select_by_visible_text('Ukraine')

        shipping_method_dropdown = self.chrome.find_element_by_css_selector(Locators.select_shipping_method)
        Select(shipping_method_dropdown).select_by_visible_text('Air')

        # Check if "Shipping type" dropdown doesn't have validation message
        assert self.chrome.find_element_by_css_selector(Locators.shipping_type_error).text == ''

        shipping_type_dropdown = self.__return__visible__element__(By.CSS_SELECTOR, Locators.select_shipping_type)
        shipping_type_dropdown_select = self.chrome.find_element_by_css_selector(Locators.shipping_type_dropdown_default)

        assert shipping_type_dropdown.is_displayed()
        # Check if default option is "Select shipping type"
        assert shipping_type_dropdown_select.text == self.shipping_type_list[0]

        # Check if drop-down menu has pre-defined elements
        shipping_types = self.chrome.find_elements_by_css_selector(Locators.all_shipping_types)
        i = 0
        for shipping_type in shipping_types:
            assert shipping_type.text == self.shipping_type_list[i]
            i = i + 1

    def test_check_calculations(self):
        self.__return__visible__element__(By.LINK_TEXT, Locators.calculation_link).click()
        sleep(2)  # wait for scrolling page down

        countries_dropdown = self.chrome.find_element_by_css_selector(Locators.select_country)
        Select(countries_dropdown).select_by_visible_text('Ukraine')

        shipping_method_dropdown = self.chrome.find_element_by_css_selector(Locators.select_shipping_method)
        Select(shipping_method_dropdown).select_by_visible_text('Sea')

        shipping_type_dropdown = self.chrome.find_element_by_css_selector(Locators.select_shipping_type)
        Select(shipping_type_dropdown).select_by_visible_text('Home delivery')

        self.chrome.find_element_by_css_selector(Locators.weight_field).send_keys('22')

        self.chrome.find_element_by_css_selector(Locators.submit_form_button).click()

        country_field_error = self.chrome.find_element_by_css_selector(Locators.county_error).text
        shipping_method_error = self.chrome.find_element_by_css_selector(Locators.shipping_method_error).text
        shipping_type_error = self.chrome.find_element_by_css_selector(Locators.shipping_type_error).text
        weight_field_error = self.chrome.find_element_by_css_selector(Locators.weight_error).text
        sleep(1) # wait for calculation of total cost
        shipping_cost = self.chrome.find_element_by_css_selector(Locators.shipping_cost).text
        total_cost = self.chrome.find_element_by_css_selector(Locators.total_cost).text

        assert country_field_error == ''
        assert shipping_method_error == ''
        assert shipping_type_error == ''
        assert weight_field_error == ''
        assert shipping_cost == '$ 76.16'
        assert total_cost == '$ 76.16'

    def setup_method(self):
        self.chrome.find_element_by_css_selector(Locators.logo).click()

    @classmethod
    def teardown_class(cls):
        cls.chrome.close()
        pass

    def __return__visible__element__(self, locator_type, locator):
        return WebDriverWait(self.chrome, 5)\
            .until(EC.visibility_of_element_located((locator_type, locator)))

