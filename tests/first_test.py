
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Setup — open Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Navigate to guru99 Bank demo
driver.get("https://demo.guru99.com/V4/index.php")

# Wait 2 seconds so you can see it load
time.sleep(2)

# Print the page title to confirm it loaded
print("Page title:", driver.title)

# Find the username field and type in it
driver.find_element(By.NAME, "uid").send_keys("mngr123")

# Find the password field and type in it
driver.find_element(By.NAME, "password").send_keys("wrongpassword")

# Find the login button and click it
driver.find_element(By.NAME, "btnLogin").click()

# Wait 2 seconds
time.sleep(2)

# Print current URL after clicking login
print("URL after login attempt:", driver.current_url)

# Close browser
driver.quit()
print("Test complete.")