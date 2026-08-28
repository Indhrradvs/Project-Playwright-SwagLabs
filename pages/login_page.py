class LoginPage:

    # Constructor
    def __init__(self, my_page):
        self.page = my_page
        self.username_input = my_page.locator("#user-name")
        self.password_input = my_page.locator("#password")
        self.login_button = my_page.locator("#login-button")

    def goto(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
