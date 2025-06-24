import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"
        self.search_box = (By.NAME, "q")

    def load(self):
        self.driver.get(self.url)

    time.sleep(5)

    #def is_loaded(self):
        # Wait up to 10 seconds for the search box
        #WebDriverWait(self.driver, 10).until(
        #    EC.presence_of_element_located(self.search_box)
        #)
        #return True

    def get_title(self):
        return self.driver.title