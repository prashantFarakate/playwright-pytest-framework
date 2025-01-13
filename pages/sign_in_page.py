from playwright.sync_api import Page
from pages.base_page import BasePage

class SignInPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self.email_input = "input[name='email']"
        self.continue_button = "button:has-text('Continue')"
        self.password_input = "input[name='password']"
        self.signin_button = "button:has-text('Sign in')"
        # self.error_message = 'span:has-text("We don\'t recognise that email")'
        self.error_message = "div.sb-form-message--error:has-text('We don\\'t recognise that email')"

    def enter_email(self, email):
        self.fill(self.email_input, email)

    def click_continue(self):
        self.click(self.continue_button)

    def enter_password(self, password):
        self.fill(self.password_input, password)

    def click_signin(self):
        self.click(self.signin_button)

