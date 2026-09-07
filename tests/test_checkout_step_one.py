from playwright.sync_api import expect
from pages.checkout_step_two_page import CheckoutStepTwoPage
import pytest

@pytest.mark.smoke
def test_step_one_checkout_title(checkout_step_one_page):
    expect(checkout_step_one_page.checkout_label).to_have_text(
        "Checkout: Your Information"
    )

@pytest.mark.regression
def test_empty_field_validation(checkout_step_one_page):
    checkout_step_one_page.click_continue()
    expect(checkout_step_one_page.error_message).to_have_text(
        "Error: First Name is required"
    )


def test_cancel_checkout(checkout_step_one_page):
    cart_page = checkout_step_one_page.click_cancel()
    expect(cart_page.cart_title_label).to_have_text("Your Cart")

@pytest.mark.smoke
def test_verify_checkout_step_two_title(checkout_step_two_page: CheckoutStepTwoPage):
    expect(checkout_step_two_page.checkout_label).to_have_text("Checkout: Overview")
