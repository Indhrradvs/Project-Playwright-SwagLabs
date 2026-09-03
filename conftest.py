import pytest
from playwright.sync_api import Page
from config.env import settings
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


@pytest.fixture
def logged_in_inventory_page(page: Page):
    login_page = LoginPage(
        page
    )  # Created Loginpage object and passing the page object to it
    login_page.goto(settings.base_url)
    login_page.login(settings.username, settings.password)

    inventory_page = InventoryPage(page)  # InventoryPage object created
    return inventory_page


@pytest.fixture
def cart_page_with_items(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Test.allTheThings() T-Shirt (Red)",
    ]

    for item in items_to_add:
        inventory_page.add_to_cart_by_name(item)

    inventory_page.cart_icon.click()

    cart_page = CartPage(inventory_page.page)
    return cart_page


@pytest.fixture
def checkout_step_one_page(cart_page_with_items):
    cart_page_with_items.cart_checkout.click()
    return CheckoutStepOnePage(cart_page_with_items.page)

@pytest.fixture
def checkout_step_two_page(checkout_step_one_page):
    return checkout_step_one_page.fill_info_and_continue('Frank', 'Martin', '1234')