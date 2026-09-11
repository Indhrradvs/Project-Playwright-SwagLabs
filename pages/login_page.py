from pages.base_page import BasePage


class LoginPage(BasePage):

    # Constructor
    def __init__(self, my_page):
        super().__init__(
            my_page
        )  # required: sets self.page via BasePage, otherwise goto() breaks
        self.username_input = my_page.locator("#user-name")
        self.password_input = my_page.locator("#password")
        self.login_button = my_page.locator("#login-button")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
