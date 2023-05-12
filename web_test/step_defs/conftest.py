import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pytest_bdd import given, then, parsers
from web_test.features.lib.pages.base import BasePage


# Parser for the console browser argument
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="Chrome",
        help="Browser for test execution", choices=["Chrome", "Firefox", "Edge"]
    )


# Set the browser driver according to the arguments, or default
@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    # Chrome driver
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Firefox driver
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    # Edge driver
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise Exception('Browser not supported')

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# Navigate to page function
@given(parsers.parse('I have navigated to \'BCNC\' "{page}" page'), target_fixture='navigate_to')
def navigate_to(driver, page):
    url = BasePage.PAGES.get(page)
    driver.get(url)






