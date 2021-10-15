from actions.pages import get_page_data
from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index


def build_match_link(match_information):
    pass


def get_match_links(browser):
    match_links = []
    page_data = get_page_data(browser)


def add_page_matches(browser, event, match_list):
    pass


def add_matches(browser, event, event_list):
    pass


def create_match_list(browser, event):
    match_list = []
    return add_matches(browser, event, match_list)


def record_event_matches(browser, season, division, league, team, event, stats):
    match_list = create_match_list(browser, event)