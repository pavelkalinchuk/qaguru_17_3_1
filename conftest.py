from selene import browser
import pytest


@pytest.fixture(scope="session")
def browser_start():
    print("\nОткрываем браузер с адресом 'https://www.google.com/ncr'и запускаем тесты!")
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://www.google.com/ncr')

    yield

    print("\nТестирование завершено. Закрываем браузер!")
    browser.close()
