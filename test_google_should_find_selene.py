from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(autouse='True')
def specific_browser_resolution():
    browser.config.window_width, browser.config.window_height = 1400, 600


def test_successful_search():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_wrong_request():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('adjarian khachapuri order online').press_enter()
    browser.element('[id="search"]').should_not(have.text('User-oriented Web UI browser tests in Python'))
