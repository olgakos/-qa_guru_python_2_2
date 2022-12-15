from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(autouse=True)
def browser_open_baseURL():
    browser.open('https://google.com')
    yield


@pytest.fixture(scope="session")
def browser_open_setting():
    browser.config.window_width = 800
    browser.config.window_height = 600
    yield


@pytest.fixture(scope="session")
def browser_open_setting2():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield


def test_google_positive(browser_open_setting):
    # browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_negative(browser_open_setting2):
    # browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('HouseTargaryn123').press_enter()
    browser.element('#topstuff').should(have.text(f'По запросу HouseTargaryn123 ничего не найдено'))