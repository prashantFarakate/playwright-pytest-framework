from playwright.sync_api import Page
from pages.base_page import BasePage

class SignOutPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self.sign_out_msg = page.locator("span:has-text(\"You've signed out, sorry to see you go.\")")
