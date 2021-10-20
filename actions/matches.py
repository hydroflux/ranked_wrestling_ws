from actions.pages import get_page_data
from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index


def build_match_information(match_information):
    pass


def get_match_information(browser):
    match_information = []
    page_data = get_page_data(browser)


def add_page_matches(browser, event, match_list):
    match_information = get_match_information(browser)
    match_list.extend(match_information)
    print(f'Added {str(len(match_information))} events to "{event.name}" team list.')


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