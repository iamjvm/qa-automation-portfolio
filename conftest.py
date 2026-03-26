import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")   # ✅ required for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)  # ✅ no Service, no webdriver-manager

    driver.get("https://demo.guru99.com/V4/index.php")

    yield driver

    driver.quit()


# 🔥 Screenshot on failure hook (UNCHANGED)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")

        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace(" ", "_")[:50]

            filename = f"reports/screenshots/{test_name}_{timestamp}.png"

            driver.save_screenshot(filename)

            print(f"\n📸 Screenshot saved: {filename}")