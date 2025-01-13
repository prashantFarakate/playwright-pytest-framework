import pytest
from utilities.config_reader import ConfigReader

@pytest.fixture(scope="session")
def config():
    return ConfigReader()

@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": None
    }

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
