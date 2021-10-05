from actions.divisions import open_division, open_division_leagues
from actions.leagues import create_league_list
from actions.main_menu import select_menu_option
from selenium_utilities.open import open_url

from settings.driver import create_webdriver
from settings.general_functions import script_execution
from settings.settings import headless, season, state

from variables.general import website, website_title
from variables.seasons import seasons
from variables.divisions import divisions


def execute(headless, season, state):
    browser = create_webdriver(headless)
    division = divisions[state.upper()]
    season = seasons[season.lower()]
    open_url(browser, website, website_title, 'open site')
    script_execution(browser, season.season_link())
    open_division(browser, season, division)
    open_division_leagues(browser, season, division)
    create_league_list(browser, season, division)
    return browser  # used during testing to continue working after executing function
