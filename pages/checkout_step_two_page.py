from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def __init__(self, my_page: Page):
        super().__init__(my_page)

        self.checkout_label = my_page.locator("[data-test='title']")
        self.payment_info = my_page.locator('[data-test="payment-info-label"]')
        self.payment_card_info = my_page.locator('[data-test="payment-info-value"]')
        self.shipping_info = my_page.locator('[data-test="shipping-info-label"]')
        self.shipping_delivery_info = my_page.locator(
            '[data-test="shipping-info-value"]'
        )
        self.price_total = my_page.locator('[data-test="total-info-label"]')
        self.item_total = my_page.locator('[data-test="subtotal-label"]')
        self.tax_label = my_page.locator('[data-test="tax-label"]')
        self.total_amount = my_page.locator('[data-test="total-label"]')
        # button
        self.finish_btn = my_page.locator('[data-test="finish"]')
