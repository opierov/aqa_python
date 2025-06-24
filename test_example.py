import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set path to your downloaded ChromeDriver
chrome_driver_path = ""

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")

# Set up the driver service using the local path
service = Service(executable_path=chrome_driver_path)

# Fixture that provides the Chrome driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Test that uses the driver fixture
def test_google_title(driver):
    driver.get("https://www.google.com")

    # Wait for the search input to appear (max 10 seconds)
#    WebDriverWait(driver, 10).until(
#       EC.presence_of_element_located((By.ID, "this-id-does-not-exist"))
#    )

    time.sleep(5)

    assert "Google" in driver.title