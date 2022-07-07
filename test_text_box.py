from selene import have
from selene.support.shared import browser


def test_submit_form():
    browser.open('/text-box')
    browser.element('#userName').type('yasha')
    browser.element('#userEmail').type('yashaka@gmail.com')
    browser.element('#currentAddress').type('Earth')
    browser.element('#permanentAddress').type('Universe & abroad')
    browser.element('#submit').click()
    