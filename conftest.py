import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.open('https://www.google.com/')
    browser.driver.set_window_size(1920, 1080)
