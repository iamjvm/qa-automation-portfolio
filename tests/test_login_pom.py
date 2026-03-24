from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


class TestLoginWithPOM:
    """Login tests using Page Object Model — Day 14"""

    def test_page_elements_visible(self, driver):
        """TC_AUTO_006 - All login elements visible using POM"""
        page = LoginPage(driver)
        assert page.is_username_field_displayed()
        assert page.is_password_field_displayed()
        assert page.is_login_button_displayed()
        print("TC_006 PASS — All elements visible")

    def test_invalid_login(self, driver):
        """TC_AUTO_007 - Invalid login using POM"""
        page = LoginPage(driver)
        page.login("wronguser", "wrongpass")
        alert_text = page.get_alert_text()
        assert "not valid" in alert_text.lower()
        print("TC_007 PASS — Invalid login alert verified")

    def test_empty_username(self, driver):
        """TC_AUTO_008 - Empty username using POM"""
        page = LoginPage(driver)
        page.login("", "anypassword")
        alert_text = page.get_alert_text()
        assert alert_text is not None
        print("TC_008 PASS — Empty username handled")

    def test_empty_password(self, driver):
        """TC_AUTO_009 - Empty password using POM"""
        page = LoginPage(driver)
        page.login("mngr123", "")
        assert page.is_login_blocked(), "Expected login to be blocked with empty password"
        print("TC_009 PASS — Empty password blocked, stayed on login page")

    def test_username_field_accepts_input(self, driver):
        """TC_AUTO_010 - Username field works via POM"""
        page = LoginPage(driver)
        page.enter_username("testuser")
        field = driver.find_element(*LoginPage.UID_FIELD)
        assert field.get_attribute("value") == "testuser"
        print("TC_010 PASS — Username field works via POM")
