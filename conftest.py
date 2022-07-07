import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 3
    browser.driver.set_window_size(1920, 1080)

