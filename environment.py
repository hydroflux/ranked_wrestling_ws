from actions.divisions import open_division, open_division_leagues
from selenium_utilities.open import open_url

from settings.driver import create_webdriver
from settings.general_functions import script_execution

from variables.general import website, website_title
from variables.seasons import seasons
from variables.divisions import divisions

# Temporary bandaid while in development
headless = False

def execute(headless, season, state):
    browser = create_webdriver(headless)
    open_url(browser, website, website_title, 'open site')
    script_execution(browser, seasons[season.lower()].season_link())
    division = divisions[state.upper()]
    open_division(browser, season, division)
    open_division_leagues(browser, season, division)
    return browser  # used during testing to continue working after executing function
