class LoginPage:

    def __init__(self, page):

        self.page = page

        self.login_btn = "text=Log In"

        self.email_input = "#email"

        self.password_input = "#password"

        self.submit_btn = "#login_submit"

    def load(self):

        self.page.goto("https://www.careerflow.ai/")

    def click_login(self):

     login_button = self.page.locator("text=Log In").nth(1)

     login_button.wait_for()

     login_button.click()

    def enter_email(self, email):

        self.page.fill(self.email_input, email)

    def enter_password(self, password):

        self.page.fill(self.password_input, password)

    def submit_login(self):

        self.page.click(self.submit_btn)