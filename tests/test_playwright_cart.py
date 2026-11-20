import pytest
from playwright.sync_api import expect
from pages.saucedemo import LoginPage


@pytest.mark.playwright
def test_add_and_remove_product(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.locator("[data-test='inventory-list']")).to_be_visible()
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
    page.locator("[data-test='remove-sauce-labs-backpack']").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_count(0)


@pytest.mark.playwright
def test_cart_item_visible(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    page.locator("[data-test='shopping-cart-link']").click()
    expect(page.locator("[data-test='inventory-item-name']").filter(has_text="Sauce Labs Bike Light")).to_have_text("Sauce Labs Bike Light")