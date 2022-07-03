import pytest
from selene import driver
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def before_all():
    browser.open('https://www.google.com/')
    driver.maximize_window()