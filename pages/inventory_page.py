from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
  
  def __init__(self, my_page:Page):
    super().__init__(my_page) # sets self.page via BasePage
    
    self.page_title = my_page.locator(".title")
    self.inventory_items = my_page.locator(".inventory_item")
    self.item_name = my_page.locator(".inventory_item_name")
    self.item_prices = my_page.locator(".inventory_item_price")
    self.add_to_cart_buttons = my_page.locator("button", has_text="Add to cart")
    self.cart_icon = my_page.locator(".shopping_cart_link")
    self.cart_items_count = my_page.locator(".shopping_cart_badge")
    self.sort_dropdown = my_page.locator("[data-test='product-sort-container']")
    
  def add_to_cart_by_name(self, product_name: str): # product_name: custom parameter, test passes the item title as a string
    item = self.page.locator(".inventory_item", has_text = product_name)
    item.get_by_role("button", name="Add to cart").click()
   