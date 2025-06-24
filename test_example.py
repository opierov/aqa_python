import pytest
from pages.google_page import GooglePage

def test_google_title(driver):
    page = GooglePage(driver)
    page.load()
    assert page.is_loaded()
    assert "Google" in page.get_title()