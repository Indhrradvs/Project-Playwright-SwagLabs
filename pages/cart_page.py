from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, my_page:Page):
        super().__init__(my_page)

        self.cart_title_label = my_page.locator("[data-test='title']")
        self.cart_quantity_label = my_page.locator("[data-test='cart-quantity-label']")
        self.cart_description_label = my_page.locator("[data-test='cart-desc-label']")
        self.cart_total_items = my_page.locator(".cart_item")
        self.cart_item_quantity_label = my_page.locator("[data-test='item-quantity']")

        # Buttons
        self.cart_remove_item = my_page.locator("button", has_text='Remove')
        #self.cart_remove_item = my_page.locator("button:has_text('Remove')") #Remove if this fails
        self.cart_continue_shopping = my_page.locator("[data-test='continue-shopping']")
        self.cart_checkout = my_page.locator("[data-test='checkout']")
