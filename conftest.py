import pytest
from playwright.sync_api import Page
from config.env import settings
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def logged_in_inventory_page(page: Page):
    login_page = LoginPage(page) #Created Loginpage object and passing the page object to it
    login_page.goto(settings.base_url)
    login_page.login(settings.username, settings.password)

    inventory_page = InventoryPage(page) #InventoryPage object created
    return inventory_page