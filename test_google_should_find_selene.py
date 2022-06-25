from selene import have
from selene.support.shared import browser
from selenium.webdriver.chrome import options

browser.open('https://www.google.com/')
options.add_argument('window-size=1920x1080');
browser.element('[name="q"]').type('selene').press_enter()
browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))


def find_selene_positive_test():
    browser.open('https://www.google.com/')
    options.add_argument('window-size=1920x1080');
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))


def find_selene_negative_test():
    search = '94858gfjhjnbx.f,cb'
    browser.element('[name="q"]').type(search).press_enter()
    browser.element('#search').should(have.text('По запросу ' + search + ' ничего не найдено.'))
