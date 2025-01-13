from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        # Locators
        self.sign_in_button = "span:has-text('Sign In')"
        self.your_account_button = "button:has-text('Your Account')"
        self.sign_out_button = "a:has-text('Sign Out')"
        self.search_button = "button[aria-label='Search BBC']"


    def click_sign_in(self):
        self.click(self.sign_in_button)

    def navigate_to_home_page(self, url):
        self.navigate(url)

    def click_your_account(self):
        self.click(self.your_account_button)

    def click_sign_out(self):
        self.click(self.sign_out_button)

    def assert_links_visible(self, links_text_list):
        for item in links_text_list:
            links = self.page.locator(f'a:text("{item}")')
            assert links.count() > 0, f"{item} link not found"
            for i in range(links.count()):
                assert links.nth(i).is_visible(), f"{item} link at index {i} is not visible"

    def is_search_visible(self):
        return self.is_visible(self.search_button)







