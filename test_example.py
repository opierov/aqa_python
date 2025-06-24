import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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

    time.sleep(5)

    assert "Google" in driver.title