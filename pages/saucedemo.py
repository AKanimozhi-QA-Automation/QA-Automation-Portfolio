from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)
        expect(self.page.locator("[data-test='login-button']")).to_be_visible()

    def login(self, username: str, password: str):
        self.page.locator("[data-test='username']").fill(username)
        self.page.locator("[data-test='password']").fill(password)
        self.page.locator("[data-test='login-button']").click()
