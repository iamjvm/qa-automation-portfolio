import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


class TestLoginWithPOM:
    """Login tests using Page Object Model — Day 14"""

    @pytest.mark.smoke
    def test_page_elements_visible(self, driver):
        """TC_AUTO_006 - All login elements visible using POM"""
        page = LoginPage(driver)
        assert page.is_username_field_displayed()
        assert page.is_password_field_displayed()
        assert page.is_login_button_displayed()
        print("TC_006 PASS — All elements visible")

    @pytest.mark.negative
    def test_invalid_login(self, driver):
        """TC_AUTO_007 - Invalid login using POM"""
        page = LoginPage(driver)
        page.login("wronguser", "wrongpass")
        alert_text = page.get_alert_text()
        assert "not valid" in alert_text.lower()
        print("TC_007 PASS — Invalid login alert verified")

    @pytest.mark.negative
    def test_empty_username(self, driver):
        """TC_AUTO_008 - Empty username using POM"""
        page = LoginPage(driver)
        page.login("", "anypassword")
        alert_text = page.get_alert_text()
        assert alert_text is not None
        print("TC_008 PASS — Empty username handled")

    @pytest.mark.negative
    def test_empty_password(self, driver):
        """TC_AUTO_009 - Empty password using POM"""
        page = LoginPage(driver)
        page.login("mngr123", "")
        assert page.is_login_blocked(), "Expected login to be blocked with empty password"
        print("TC_009 PASS — Empty password blocked, stayed on login page")

    @pytest.mark.regression
    def test_username_field_accepts_input(self, driver):
        """TC_AUTO_010 - Username field works via POM"""
        page = LoginPage(driver)
        page.enter_username("testuser")
        field = driver.find_element(*LoginPage.UID_FIELD)
        assert field.get_attribute("value") == "testuser"
        print("TC_010 PASS — Username field works via POM")


class TestLoginDataDriven:
    """Data-driven login tests using POM — Day 15"""

    @pytest.mark.negative
    @pytest.mark.parametrize("username, password", [
        ("",           "anypassword"),
        ("mngr655759", ""),
        ("wronguser",  "wrongpassword"),
        pytest.param("MNGR655759", "YzYsEza",
                     marks=pytest.mark.xfail(reason="Bug: login is case-insensitive")),
        pytest.param("mngr655759 ", "YzYsEza",
                     marks=pytest.mark.xfail(reason="Bug: trailing space not trimmed")),
    ])
    def test_invalid_login_combinations(self, driver, username, password):
        """TC_AUTO_011-015 - Various invalid login combinations"""
        page = LoginPage(driver)
        page.login(username, password)

        wait = WebDriverWait(driver, 5)
        try:
            wait.until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert alert_text is not None
        except:
            assert "Managerhomepage" not in driver.current_url, \
                f"Login unexpectedly succeeded for user='{username}'"