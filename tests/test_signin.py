import json
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from pages.sign_out_page import SignOutPage
from utilities.logger import bbc_logs
logger = bbc_logs()
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("User SignIn Functionality")
@allure.feature("Login Page")
@allure.title("Verify SignIn with valid credentials")
@pytest.mark.smoke
def test_signin(page, config):

    logger.info("Starting Sign in test")
    home_page = HomePage(page)
    signin_page = SignInPage(page)
    sign_out_page = SignOutPage(page)

    home_page.navigate_to_home_page(config.get_url())
    home_page.click_sign_in()
    signin_page.enter_email(config.get_username())
    signin_page.click_continue()
    signin_page.enter_password(config.get_password())
    signin_page.click_signin()
    logger.info("Sign-in successful")

    expected_title = "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio"
    assert home_page.page.title() == expected_title

    # Sign out and verify the message
    home_page.click_your_account()
    home_page.click_sign_out()
    expect(sign_out_page.sign_out_msg).to_contain_text("You've signed out, sorry to see you go.")
    logger.info("Sign-out successful")
    logger.info("Sing-in testcase passed successfully")

@allure.severity(allure.severity_level.NORMAL)
@allure.story("User SignIn Functionality")
@allure.feature("Login Page")
@allure.title("Verify SignIn with invalid credentials")
def test_invalid_signin(page, config):
    logger.info("Starting invalid sign-in test")
    home_page = HomePage(page)
    signin_page = SignInPage(page)

    with open("test_data/invalid_cred.json") as f:
        credentials = json.load(f)

    home_page.navigate_to_home_page(config.get_url())
    home_page.click_sign_in()
    signin_page.enter_email(credentials["invalid_username"])
    signin_page.click_continue()

    # Verify error message is visible
    assert home_page.page.locator(signin_page.error_message).is_visible(), "Error message is not visible for invalid credentials"
    logger.info("Invalid credentials test passed")


