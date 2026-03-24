from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def test_page_loads(self,driver):
        """TC_001 - Page loads and username field is present"""
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "uid")))
        assert driver.title !=""
        print("TC_001 PASS - Page loaded")
        
    def test_invalid_login(self, driver):
        """TC_002 - Invalid credentials show error alert"""
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.NAME, "uid").send_keys("invalidUser")
        driver.find_element(By.NAME, "password").send_keys("invalidPass")
        driver.find_element(By.NAME, "btnLogin").click()
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "not valid" in alert.text.lower()
        alert.accept()
        print("TC_002 PASS - Invalid login alert verified")

    def test_username_field_accepts_input(self, driver):
        """TC_003 - Username field accepts typed input"""
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "uid")))
        uid_field = driver.find_element(By.NAME, "uid")
        uid_field.send_keys("testuser10")
        assert uid_field.get_attribute("value") == "testuser10"
        print("TC_003 PASS - Username field works")

    def test_password_field_accepts_input(self, driver):
        """TC_004 - Password field accepts typed input"""
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "password")))
        pwd_field = driver.find_element(By.NAME, "password")
        pwd_field.send_keys("mypassword")
        assert pwd_field.get_attribute("value") == "mypassword"
        print("TC_004 PASS - Password field works")

    def test_login_button_visible(self, driver):
        """TC_005 - Login button is visible and enabled"""
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "btnLogin")))
        btn = driver.find_element(By.NAME, "btnLogin")
        assert btn.is_displayed()
        assert btn.is_enabled()
        print("TC_005 PASS — Login button visible and clickable")