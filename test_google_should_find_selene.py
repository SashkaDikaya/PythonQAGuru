import pytest
from selene import have, driver
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def before_all():
    browser.config.browser_name = 'firefox'
    browser.open('https://www.google.com/')


def find_selene_positive_test():

    driver.maximize_window()
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))



def find_selene_negative_test():
    search = '94858gfjhjnbx.f,cb'
    browser.element('[name="q"]').type(search).press_enter()
    browser.element('#search').should(have.text('По запросу ' + search + ' ничего не найдено.'))
