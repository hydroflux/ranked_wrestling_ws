from selenium_utilities.open import open_url

from settings.driver import create_webdriver

from variables.variables import website, website_title

def execute(headless):
    browser = create_webdriver(False)
    open_url(browser, website, website_title, 'open site')
