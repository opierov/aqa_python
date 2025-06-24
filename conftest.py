import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Replace with your actual path
chrome_driver_path = "/Users/oleksandrpierov/Desktop/tools/selenium/ChromeDriver 137.0.7151.119/chromedriver"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()