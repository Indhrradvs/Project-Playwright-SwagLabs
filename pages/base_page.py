from playwright.sync_api import Page

class BasePage:
  def __init__(self, my_page:Page):
    self.page = my_page
    
  def goto(self, url):
    self.page.goto(url)
    