from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from config.env import settings


def test_verify_cart_page_title(cart_page_with_items):
    expect(cart_page_with_items.cart_title_label).to_have_text("Your Cart")


def test_verify_cart_page_table_columns(cart_page_with_items):
    expect(cart_page_with_items.cart_quantity_label).to_have_text("QTY")
    expect(cart_page_with_items.cart_description_label).to_have_text("Description")


def test_verify_cart_page_add_items_count(cart_page_with_items):
    expect(cart_page_with_items.cart_total_items).to_have_count(3)


def test_verify_cart_page_each_item_quantity(cart_page_with_items):
    expect(cart_page_with_items.cart_item_quantity_label).to_have_count(3)

    quantity_count = cart_page_with_items.cart_item_quantity_label.count()

    for q in range(quantity_count):
        expect(cart_page_with_items.cart_item_quantity_label.nth(q)).to_have_text("1")


def test_verify_cart_page_remove_button(cart_page_with_items):
    expect(cart_page_with_items.cart_remove_btn).to_have_count(3)

    remove_btn_count = cart_page_with_items.cart_remove_btn.count()

    for item in range(remove_btn_count):
        expect(cart_page_with_items.cart_remove_btn.nth(item)).to_have_text("Remove")
        expect(cart_page_with_items.cart_remove_btn.nth(item)).to_be_enabled()


def test_verify_cart_page_footer_btns(cart_page_with_items):
    # Continue shopping
    expect(cart_page_with_items.cart_continue_shopping).to_be_visible()
    expect(cart_page_with_items.cart_continue_shopping).to_be_enabled()
    expect(cart_page_with_items.cart_continue_shopping).to_have_text(
        "Continue Shopping"
    )

    # Check out
    expect(cart_page_with_items.cart_checkout).to_be_visible()
    expect(cart_page_with_items.cart_checkout).to_be_enabled()
    expect(cart_page_with_items.cart_checkout).to_have_text("Checkout")


def test_continue_shopping_navigates_to_inventory(cart_page_with_items):
    cart_page_with_items.cart_continue_shopping.click()

    inventory_page = InventoryPage(cart_page_with_items.page)
    expect(inventory_page.page_title).to_have_text("Products")


def test_checkout_navigates_to_checkout_page(cart_page_with_items):
    cart_page_with_items.cart_checkout.click()
    expect(cart_page_with_items.page).to_have_url(
        f"{settings.base_url}/checkout-step-one.html"
    )
