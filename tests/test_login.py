from playwright.sync_api import Page, expect
from config.env import settings
from pages.login_page import LoginPage


def test_loginPage(page: Page):
    """
    # login_page = LoginPage(page)
    # LoginPage → Class
    # LoginPage(page) → Creates a LoginPage object
    # page → Existing Playwright Page object
    # login_page → Reference to the newly created LoginPage object
    """
    login_page = LoginPage(page)
    login_page.goto(settings.base_url)
    login_page.login(settings.username, settings.password)

    # Verifying the URL
    expect(page).to_have_url(
        f"{settings.base_url}inventory.html"
    )  # '/' already added to url

    # Verifying title of the section
    expect(page.locator(".title")).to_have_text("Products")
