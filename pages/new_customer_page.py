from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewCustomerPage:
    """Page Object for guru99 Bank New Customer page"""

    # Locators — verified from live site
    CUSTOMER_NAME = (By.NAME, "name")
    DOB_FIELD     = (By.NAME, "dob")
    ADDRESS       = (By.NAME, "addr")
    CITY          = (By.NAME, "city")
    STATE         = (By.NAME, "state")
    PIN           = (By.NAME, "pinno")
    MOBILE        = (By.NAME, "telephoneno")
    EMAIL         = (By.NAME, "emailid")
    PASSWORD      = (By.NAME, "password")
    SUBMIT_BTN    = (By.NAME, "sub")
    RESET_BTN     = (By.NAME, "res")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_name(self, name):
        f = self.driver.find_element(*self.CUSTOMER_NAME)
        f.clear()
        f.send_keys(name)

    def enter_dob(self, dob):
        f = self.driver.find_element(*self.DOB_FIELD)
        f.clear()
        f.send_keys(dob)

    def enter_address(self, address):
        f = self.driver.find_element(*self.ADDRESS)
        f.clear()
        f.send_keys(address)

    def enter_city(self, city):
        f = self.driver.find_element(*self.CITY)
        f.clear()
        f.send_keys(city)

    def enter_state(self, state):
        f = self.driver.find_element(*self.STATE)
        f.clear()
        f.send_keys(state)

    def enter_pin(self, pin):
        f = self.driver.find_element(*self.PIN)
        f.clear()
        f.send_keys(pin)

    def enter_mobile(self, mobile):
        f = self.driver.find_element(*self.MOBILE)
        f.clear()
        f.send_keys(mobile)

    def enter_email(self, email):
        f = self.driver.find_element(*self.EMAIL)
        f.clear()
        f.send_keys(email)

    def enter_password(self, password):
        f = self.driver.find_element(*self.PASSWORD)
        f.clear()
        f.send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def click_reset(self):
        self.driver.find_element(*self.RESET_BTN).click()

    def fill_form(self, name, dob, address, city, state, pin, mobile, email, password):
        """Fill all fields in one go"""
        self.enter_customer_name(name)
        self.enter_dob(dob)
        self.enter_address(address)
        self.enter_city(city)
        self.enter_state(state)
        self.enter_pin(pin)
        self.enter_mobile(mobile)
        self.enter_email(email)
        self.enter_password(password)
