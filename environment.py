from actions import open_division
from selenium_utilities.open import open_url

from settings.driver import create_webdriver
from settings.general_functions import script_execution

from variables.general import website, website_title
from variables.seasons import seasons

headless = False

def execute(headless, season, state):
    browser = create_webdriver(headless)
    open_url(browser, website, website_title, 'open site')
    script_execution(browser, seasons[season.lower()].season_link())
    division = open_division(browser, state)

