import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="module")
def browser_chromium(playwright):
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope="module")
def browser_firefox(playwright):
    browser = playwright.firefox.launch()
    yield browser
    browser.close()

@pytest.fixture
def operator_context(browser_chromium):
    context = browser_chromium.new_context()
    yield context
    context.close()

@pytest.fixture
def customer_context(browser_firefox):
    context = browser_firefox.new_context()
    yield context
    context.close()

@pytest.fixture
def operator_page(operator_context):
    page = operator_context.new_page()
    yield page
    page.close()

@pytest.fixture
def customer_page(customer_context):
    page = customer_context.new_page()
    yield page
    page.close()