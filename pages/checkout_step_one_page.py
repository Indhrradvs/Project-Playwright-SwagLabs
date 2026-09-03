from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def __init__(self, my_page: Page):
        super().__init__(my_page)

        self.checkout_label = my_page.locator("[data-test='title']")

        # Input fields
        self.first_name_field = my_page.locator('[data-test="firstName"]')
        self.last_name_field = my_page.locator('[data-test="lastName"]')
        self.zip_code_field = my_page.locator('[data-test="postalCode"]')

        # Field validation message
        self.error_message = my_page.locator('[data-test="error"]')

        # footer section buttons
        self.cancel_btn = my_page.locator('[data-test="cancel"]')
        self.continue_btn = my_page.locator('[data-test="continue"]')

    def click_continue(self):
        self.continue_btn.click()

    def click_cancel(self):
        self.cancel_btn.click()
        from pages.cart_page import CartPage

        return CartPage(
            self.page
        )  # Need this page object to verify the CartPage title when we click on cancel button

    def fill_info_and_continue(self, first_name: str, last_name: str, zipcode: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zip_code_field.fill(zipcode)
        self.continue_btn.click()
        from pages.checkout_step_two_page import CheckoutStepTwoPage

        return CheckoutStepTwoPage(self.page)
