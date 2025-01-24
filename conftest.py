import os
import pytest
from pytest_html.extras import image
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_path = f"{screenshots_dir}/{item.name}.png"

        # Access the page fixture dynamically and take a screenshot
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=screenshot_path)

        # Attach the screenshot to the pytest-html report
        if os.path.exists(screenshot_path):
            extra = getattr(report, 'extra', [])
            extra.append(image(screenshot_path))
            report.extra = extra




