import pytest
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"

@pytest.mark.ui
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("standard_user", "secret_sauce")
    
    # Validate successful login by checking URL change
    assert "inventory.html" in page.url, "Login failed"

@pytest.mark.ui
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("invalid_user", "wrong_password")
    
    # Validate error message
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match" in error_message, "Error message not displayed"
