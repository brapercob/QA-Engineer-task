from selenium.webdriver.common.by import By


class BasePage:

    BASE = 'https://bcncgroup.com'

    # Dictionary of pages for the BCNC web
    PAGES = {"Home": BASE + '/',
             "Who we are": BASE + '/who-we-are'}

    # Locator for paragraphs
    paragraphs = (By.XPATH, "//div[@class='text']")

    def __init__(self, driver):
        self.driver = driver

    def get_paragraphs(self):
        return self.driver.find_elements(*BasePage.paragraphs)
