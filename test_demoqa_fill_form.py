from selene import have
from selene.support import webdriver
from selene.support.shared import browser



browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()
browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
browser.element('#firstName').type('Aleksandra')
browser.element('#lastName').type('Dikaya')
browser.element('#userEmail').type('dikaya@gmail.com')
browser.element('//div[@class="col-md-9 col-sm-12"]//label[contains(text(), "Female")]').click()
browser.element('#userNumber').type('1236547890')
browser.element('#dateOfBirthInput').click()

browser.element('//select[@class="react-datepicker__month-select"]/option[contains(text(), "December")]').click()
browser.element('//select[@class="react-datepicker__year-select"]/option[contains(text(), "1987")]').click()
browser.element('//div[contains(@aria-label, "December 24th, 1987")]').click()

browser.element('#subjectsInput').type('Maths').press_enter()
browser.element('#hobbiesWrapper').should(have.text('Music')).click()
browser.element('#currentAddress').type('Saint-P, Red kursant, house 4, app 15')
browser.element('#state').click()
browser.element('#react-select-3-input').type('NCR').press_enter()
browser.element('#city').click()
browser.element('#react-select-4-input').type('Delhi').press_enter()
browser.element('#submit').click()

browser.element('.table-responsive').should(have.text('Aleksandra Dikaya'))
browser.element('.table-responsive').should(have.text('dikaya@gmail.com'))
browser.element('.table-responsive').should(have.text('Female'))
browser.element('.table-responsive').should(have.text('1236547890'))
browser.element('.table-responsive').should(have.text('24 December,1987'))
browser.element('.table-responsive').should(have.text('Maths'))
browser.element('.table-responsive').should(have.text('Music'))
browser.element('.table-responsive').should(have.text('Saint-P, Red kursant, house 4, app 15'))
browser.element('.table-responsive').should(have.text('NCR Delhi'))

browser.element('#closeLargeModal').click()



