from playwright.sync_api import expect
from pages.checkout_step_two_page import CheckoutStepTwoPage
import pytest

def test_verify_checkout_title(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.checkout_label).to_have_text("Checkout: Overview")
 
@pytest.mark.regression  
def test_verify_payment_info(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.payment_info).to_have_text("Payment Information:")
  
def test_verify_payment_card(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.payment_card_info).to_have_text("SauceCard #31337")
  
def test_verify_shipping_info(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.shipping_info).to_have_text("Shipping Information:")
  
def test_verify_shipping_delivery(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.shipping_delivery_info).to_have_text("Free Pony Express Delivery!")
  
def test_verify_price_total(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.price_total).to_have_text("Price Total")

@pytest.mark.regression   
def test_verify_item_total(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.item_total).to_have_text("Item total: $55.97")
  
def test_verify_tax_total(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.tax_label).to_have_text("Tax: $4.48")
  
def test_verify_summary_total(checkout_step_two_page:CheckoutStepTwoPage):
  expect(checkout_step_two_page.total_amount).to_have_text("Total: $60.45")

@pytest.mark.regression 
def test_verify_complete_title(checkout_step_two_page_finish):
  expect(checkout_step_two_page_finish.checkout_final_page_label).to_have_text("Checkout: Complete!")
  
  
  