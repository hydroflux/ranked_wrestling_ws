from classes.Match import Match
from classes.Stat import Stat

from selenium_utilities.locators import (locate_elements_by_class_name,
                                         locate_elements_by_tag_name)

from variables.general import row_class_name, row_data_tag

from actions.pages import get_page_data


def build_dual_match_information(match_information):
    pass


def get_dual_summary_information(browser):
    dual_summary_information = []
    page_data = get_page_data(browser, False)
    match_rows = locate_elements_by_class_name(page_data, row_class_name, 'match rows')
    for row in match_rows:
        match_information = locate_elements_by_tag_name(row, row_data_tag, "match information")
        dual_summary_information.append(build_dual_match_information(match_information))
    return dual_summary_information


def add_page_dual_matches(browser, event, match_list):
    dual_summary_information = get_dual_summary_information(browser)
    match_list.extend(dual_summary_information)
    print(f'Added {str(len(dual_summary_information))} events to "{event.name}" team list.')


# nearly identical to 'add_matches' in the 'matches' script
def add_dual_matches(browser, event, match_list):
    add_page_dual_matches(browser, event, match_list)
    while len(match_list) < event.number_matches:  # Currently irrelevant, need to update in order to capture number_matches
        print('Encountered multiple match pages, please review, update code, & re-start')
        input('Press enter to continue...')
    return match_list


def create_dual_match_list(browser, event):
    match_list = []
    return add_dual_matches(browser, event, match_list)


def update_team_events():  # ?????
    pass


def report_duals():
    pass


def open_event():
    pass


def search_event():
    pass


def record_duals():
    pass


def record_event_duals(browser, division, league, team, event, stats):
    pass
    # General Variables
    official = ''
    comment = ''
    # Team One Variables
    team_one = ''
    team_one_score = ''
    # Team Two Variables
    team_two = ''
    team_two_score = ''
    # match_list = create_dual_match_list(browser, event)
