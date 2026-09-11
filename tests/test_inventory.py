"""
Test scenarios:Inventory Page
1. Verify the 'Products' section header
2. How many items are displaying by default
3. Verify 'Add to cart' button is displaying for all the items
4. Verify the price is displaying for all available items with $ symbol
5. Verify Cart icon on the top right corner
6. Verify the filter icon (sort dropdown) on the top right corner
7. Click on the 'Add to cart' button
8. Verify the added item count is displaying on the Cart icon
"""

from playwright.sync_api import expect
import pytest


@pytest.mark.smoke
def test_verify_products_title(logged_in_inventory_page):
    expect(logged_in_inventory_page.page_title).to_have_text("Products")


def test_verify_default_items_count(logged_in_inventory_page):
    expect(logged_in_inventory_page.inventory_items).to_have_count(6)


@pytest.mark.regression
def test_add_to_cart_button_displayed_for_all_items(logged_in_inventory_page):
    expect(logged_in_inventory_page.add_to_cart_buttons).to_have_count(6)

    # Verifying 'Add to cart' button enabled for all avaialable items
    count = logged_in_inventory_page.add_to_cart_buttons.count()
    for i in range(count):
        expect(logged_in_inventory_page.add_to_cart_buttons.nth(i)).to_be_enabled()


@pytest.mark.regression
def test_verify_items_price(logged_in_inventory_page):

    prices = logged_in_inventory_page.item_prices.count()

    for p in range(prices):
        expect(logged_in_inventory_page.item_prices.nth(p)).to_contain_text("$")


def test_verify_cart_icon(logged_in_inventory_page):
    expect(logged_in_inventory_page.cart_icon).to_be_visible()


def test_verify_sort_dropdown(logged_in_inventory_page):
    expect(logged_in_inventory_page.sort_dropdown).to_be_visible()
    expect(logged_in_inventory_page.sort_dropdown).to_be_enabled()


@pytest.mark.smoke
def test_verify_add_to_cart(logged_in_inventory_page):
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Test.allTheThings() T-Shirt (Red)",
    ]  # if u want to select more, add value here

    for items in items_to_add:
        logged_in_inventory_page.add_to_cart_by_name(items)

    items_expected_count = str(len(items_to_add))
    expect(logged_in_inventory_page.cart_items_count).to_have_text(items_expected_count)
