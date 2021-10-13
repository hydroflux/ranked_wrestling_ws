from actions.pages import get_page_data
from selenium_utilities.locators import locate_element_by_class_name
from variables.general import no_records_class


def check_for_results(browser):
    page_data = get_page_data(browser, False)
    if not locate_element_by_class_name(page_data, no_records_class, "no records", quick=True): return True


def record_invalid_league(browser, division, league, stats):
    pass


def record_invalid_team(browser, division, league, team, stats):
    pass