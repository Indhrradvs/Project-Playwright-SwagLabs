from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def __init__(self, my_page: Page):
        super().__init__(my_page)

        self.checkout_label = my_page.locator("[data-test='title']")