from playwright.sync_api import expect
from pages.checkout_complete_page import CheckoutCompletePage
import pytest


def test_verify_checkout_title(checkout_step_two_page_finish: CheckoutCompletePage):
    expect(checkout_step_two_page_finish.checkout_final_page_label).to_have_text(
        "Checkout: Complete!"
    )


def test_verify_checkout_Thanks_message(
    checkout_step_two_page_finish: CheckoutCompletePage,
):
    expect(checkout_step_two_page_finish.thanks_msg).to_have_text(
        "Thank you for your order!"
    )


@pytest.mark.regression
def test_verify_checkout_confirm_message(
    checkout_step_two_page_finish: CheckoutCompletePage,
):
    expect(checkout_step_two_page_finish.order_info).to_have_text(
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    )


def test_verify_checkout_Back_Home(checkout_step_two_page_finish: CheckoutCompletePage):
    expect(checkout_step_two_page_finish.back_home_btn).to_be_visible()
    expect(checkout_step_two_page_finish.back_home_btn).to_be_enabled()
