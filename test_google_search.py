from selene import have
from selene.support.shared import browser


def test_positive_search():
    search = 'selene'
    responce = 'User-oriented Web UI browser tests in Python'
    browser.element('[name="q"]').type(search).press_enter()
    browser.element('#search').should(have.text(responce))


def test_negative_search():
    search = '94858gfjhjnbx.f,cb'
    responce = 'По запросу ' + search + ' ничего не найдено.'
    browser.element('[name="q"]').type(search).press_enter()
    browser.element('.card-section').should(have.text(responce))
