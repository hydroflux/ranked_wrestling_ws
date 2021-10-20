from actions.pages import get_page_data
from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index

from variables.general import row_class_name, row_data_tag


def split_match_summary_information(match_summary):
    pass


def build_single_match_information(match_information):
    match_summary = match_information[2].text 
    match_information = {
        "weight": match_information[1].text,
        "summary": match_summary,
        "stat_flag": match_information[3].text,
        "tw_event": match_information[4].text,
        "rounds": '',
        "winning_team": '',
        "winner": '',
        "losing_team": '',
        "loser": '',
        "results": '',
        "time": '',
        "winning_point": '',
        "losing_point": ''
    }
    return match_information


def get_match_summary_information(browser):
    match_summary_information = []
    page_data = get_page_data(browser, False)
    match_rows = locate_elements_by_class_name(page_data, row_class_name, 'match rows')
    for row in match_rows:
        match_information = locate_elements_by_tag_name(row, row_data_tag, "match information")
        match_summary_information.append(build_single_match_information(match_information))
    return match_summary_information


def add_page_matches(browser, event, match_list):
    match_summary_information = get_match_summary_information(browser)
    match_list.extend(match_summary_information)
    print(f'Added {str(len(match_summary_information))} events to "{event.name}" team list.')


def add_matches(browser, event, match_list):
    add_page_matches(browser, event, match_list)
    while len(match_list) < event.number_matches:
        print('Encountered multiple match pages, please review, update code, & re-start')
        input('Press enter to continue...')
    return match_list


def create_match_list(browser, event):
    match_list = []
    return add_matches(browser, event, match_list)


def update_event_matches(event, match_list):
    pass
    # event.number_matches = len(matches)


def record_event_matches(browser, season, division, league, team, event, stats):
    match_list = create_match_list(browser, event)