from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, my_page: Page):
        super().__init__(my_page)
        self.checkout_final_page_label = my_page.locator("[data-test='title']")
        self.thanks_msg = my_page.locator('[data-test="complete-header"]')
        self.order_info = my_page.locator('[data-test="complete-text"]')
        self.back_home_btn = my_page.locator('[data-test="back-to-products"]')
