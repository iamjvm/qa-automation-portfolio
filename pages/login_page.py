from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # ← added


class LoginPage:
    """Page Object Model for guru99 Bank Login Page"""

    # Locators — all in one place
    UID_FIELD = (By.NAME, "uid")
    PWD_FIELD = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "btnLogin")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(self.UID_FIELD))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located(self.PWD_FIELD))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_alert_text(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def is_login_blocked(self):
        """Returns True if still on login page (login was blocked)"""
        try:
            self.wait.until(EC.url_contains("index.php"))  # ← adjust if needed
            return True
        except TimeoutException:
            return False

    def is_username_field_displayed(self):
        return self.driver.find_element(*self.UID_FIELD).is_displayed()

    def is_password_field_displayed(self):
        return self.driver.find_element(*self.PWD_FIELD).is_displayed()

    def is_login_button_displayed(self):
        return self.driver.find_element(*self.LOGIN_BTN).is_displayed()