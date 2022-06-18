from selene import have
from selene.support.shared import browser

browser.open('https://www.google.com/')
browser.element('[name="q"]').type('selene').press_enter()
browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))