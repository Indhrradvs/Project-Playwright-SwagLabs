from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_verify_cart_page_title(cart_page_with_items):
    expect(cart_page_with_items.cart_title_label).to_have_text("Your Cart")


def test_verify_cart_page_table_columns(cart_page_with_items):
    expect(cart_page_with_items.cart_quantity_label).to_have_text("QTY")
    expect(cart_page_with_items.cart_description_label).to_have_text("Description")

def test_verify_cart_page_add_items_count(cart_page_with_items):
  expect(cart_page_with_items.cart_total_items).to_have_count(3)
  
  