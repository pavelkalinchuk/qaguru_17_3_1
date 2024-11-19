from selene import browser
import pytest


@pytest.fixture(scope="session")
def browser_start():
    print("\nЗапускаем браузер с адресом https://www.google.com/ncr!")
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://www.google.com/ncr')

    yield

    print("\nЗакрываем браузер!")
    browser.close()