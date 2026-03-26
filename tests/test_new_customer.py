import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.new_customer_page import NewCustomerPage


class TestNewCustomer:
    """New Customer page tests using POM — Day 15"""

    @pytest.fixture(autouse=True)
    def navigate_to_new_customer(self, driver):
        """Log in and go to New Customer page before each test"""
        page = LoginPage(driver)
        page.login("mngr655759", "YzYsEza")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("Managerhomepage"))
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

    @pytest.mark.smoke
    def test_new_customer_page_loads(self, driver):
        """TC_AUTO_016 — New Customer page loads correctly"""
        nc = NewCustomerPage(driver)
        assert nc.driver.find_element(*NewCustomerPage.CUSTOMER_NAME).is_displayed(), \
            "Customer Name field not visible"
        assert nc.driver.find_element(*NewCustomerPage.SUBMIT_BTN).is_displayed(), \
            "Submit button not visible"
        print("TC_016 PASS — New Customer page loaded")

    @pytest.mark.negative
    def test_blank_customer_name(self, driver):
        """TC_AUTO_017 — Blank customer name shows error"""
        nc = NewCustomerPage(driver)
        nc.enter_customer_name("")
        nc.driver.find_element(*NewCustomerPage.DOB_FIELD).click()
        error = driver.find_element(By.ID, "message")
        assert error.is_displayed(), \
            "Expected error message for blank name"
        print("TC_017 PASS — Blank name error shown")

    @pytest.mark.negative
    def test_numeric_customer_name(self, driver):
        """TC_AUTO_018 — Numeric customer name shows error"""
        nc = NewCustomerPage(driver)
        nc.enter_customer_name("12345")
        nc.driver.find_element(*NewCustomerPage.DOB_FIELD).click()
        error = driver.find_element(By.ID, "message")
        assert error.is_displayed(), \
            "Expected error for numeric name"
        print("TC_018 PASS — Numeric name error shown")

    @pytest.mark.negative
    def test_blank_address(self, driver):
        """TC_AUTO_019 — Blank address shows error"""
        nc = NewCustomerPage(driver)
        nc.enter_address("")
        nc.driver.find_element(*NewCustomerPage.CITY).click()
        error = driver.find_element(By.ID, "message3")
        assert error.is_displayed(), \
            "Expected error message for blank address"
        print("TC_019 PASS — Blank address error shown")

    @pytest.mark.negative
    @pytest.mark.boundary
    def test_invalid_pin_letters(self, driver):
        """TC_AUTO_020 — PIN with letters shows error"""
        nc = NewCustomerPage(driver)
        nc.enter_pin("ABCDEF")
        nc.driver.find_element(*NewCustomerPage.MOBILE).click()
        error = driver.find_element(By.ID, "message6")
        assert error.is_displayed(), \
            "Expected error for letters in PIN"
        print("TC_020 PASS — PIN letters error shown")

    @pytest.mark.negative
    @pytest.mark.boundary
    def test_invalid_pin_less_than_6_digits(self, driver):
        """TC_AUTO_021 — PIN less than 6 digits shows error"""
        nc = NewCustomerPage(driver)
        nc.enter_pin("123")
        nc.driver.find_element(*NewCustomerPage.MOBILE).click()
        error = driver.find_element(By.ID, "message6")
        assert error.is_displayed(), \
            "Expected error for PIN less than 6 digits"
        print("TC_021 PASS — Short PIN error shown")

    @pytest.mark.negative
    def test_invalid_mobile_letters(self, driver):
        """TC_AUTO_022 — Mobile with letters shows error"""
        nc = NewCustomerPage(driver)
        nc.enter_mobile("abcdefgh")
        nc.driver.find_element(*NewCustomerPage.EMAIL).click()
        error = driver.find_element(By.ID, "message7")
        assert error.is_displayed(), \
            "Expected error for letters in mobile"
        print("TC_022 PASS — Mobile letters error shown")

    @pytest.mark.regression
    def test_reset_clears_fields(self, driver):
        """TC_AUTO_023 — Reset button clears all fields"""
        nc = NewCustomerPage(driver)
        nc.enter_customer_name("Test User")
        nc.enter_city("Mumbai")
        nc.click_reset()
        name_value = driver.find_element(
            *NewCustomerPage.CUSTOMER_NAME).get_attribute("value")
        assert name_value == "", \
            f"Expected empty field after reset, got: '{name_value}'"
        print("TC_023 PASS — Reset cleared all fields")