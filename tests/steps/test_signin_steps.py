import pytest
from pytest_bdd import given, when, then, parsers, scenario
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from pages.sign_out_page import SignOutPage

# import feature file
@scenario("../features/signin.feature", "User can sign in and sign out successfully")
def test_bbc_signin():
    pass

@pytest.fixture()
def setup(page , config):
    """
        Fixture to initialize pages.
    """
    home_page = HomePage(page)
    signin_page = SignInPage(page)
    sign_out_page = SignOutPage(page)

    return home_page, signin_page, sign_out_page, config

@given('I am on the BBC Home Page')
def navigate_to_homepage(setup):
    home_page, signin_page, sign_out_page, config = setup
    home_page.navigate_to_home_page(config.get_url())

@when('I click on sign in button')
def click_signin(setup):
    home_page, signin_page, sign_out_page, config = setup
    home_page.click_sign_in()

@when('I enter my email')
def enter_email(setup):
    home_page, signin_page, sign_out_page, config = setup
    signin_page.enter_email(config.get_username())

@when('I click continue button')
def click_continue(setup):
    home_page, signin_page, sign_out_page, config = setup
    signin_page.click_continue()

@when('I enter my password')
def enter_password(setup):
    home_page, signin_page, sign_out_page, config = setup
    signin_page.enter_password(config.get_password())

@when('Click sign in button')
def click_signin_button(setup):
    home_page, signin_page, sign_out_page, config = setup
    signin_page.click_signin()


@then('I should see the BBC Home Page with correct title')
def verify_home_page_title(setup):
    home_page, signin_page, sign_out_page, config = setup
    expected_title = "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio"
    assert home_page.page.title() == expected_title

@when('I click on your account')
def click_your_account(setup):
    home_page, signin_page, sign_out_page, config = setup
    home_page.click_your_account()

@when('I click on Sign Out')
def click_sign_out(setup):
    home_page, signin_page, sign_out_page, config = setup
    home_page.click_sign_out()

@then('I should see the sign out message')
def verify_sign_out_message(setup):
    home_page, signin_page, sign_out_page, config = setup
    expect(sign_out_page.sign_out_msg).to_contain_text("You've signed out, sorry to see you go.")



