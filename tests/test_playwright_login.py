import pytest
from playwright.sync_api import expect
from pages.saucedemo import LoginPage


@pytest.mark.playwright
def test_valid_login_displays_inventory(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='inventory-list']")).to_be_visible()


@pytest.mark.playwright
def test_invalid_login_displays_error(page):
    login = LoginPage(page)
    login.open()
    login.login("invalid_user", "invalid_password")
    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username and password do not match"
    )


@pytest.mark.playwright
def test_required_username_validation(page):
    login = LoginPage(page)
    login.open()
    login.login("", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("Username is required")
