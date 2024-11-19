from selene import browser, be, have


def test_positive_text(browser_start):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text("yashaka/selene: User-oriented Web UI browser tests in Python"))


def test_negative_text(browser_start):
    browser.element('[name="q"]').clear().type('()@#').press_enter()
    browser.element('[id="botstuff"]').should(have.text("did not match any documents"))