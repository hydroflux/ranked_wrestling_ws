from actions.pages import get_page_data, get_page_handler
from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name

from variables.general import row_class_name, link_tag_name, row_data_tag

# def get_number_events(page_handler):
#     handler_text = page_handler.text
#     return int(handler_text[handler_text.rfind(' ') + 1:])


# def report_number_teams(team):
#     print(f'{str(team.number_events)} total events located for the '
#           f'"{team.name}" Team.')


# def count_events(browser, team):
#     page_handler = get_page_handler(browser)


def build_event_links(event_links, event_information):
    pass


def get_event_links(page_data):
    event_links = []
    event_rows = locate_elements_by_class_name(page_data, row_class_name, 'event rows')
    for row in event_rows:
        event_information = locate_elements_by_tag_name(row, row_data_tag, "event information")
        build_event_links(event_links, event_information)


def add_page_events(browser, team, event_list):
    page_data = get_page_data(browser, False)
    event_links = get_event_links(page_data)
    event_list.extend(event_links)
    print(f'Added {str(len(event_links))} events to "{team.name}" team list.')


def add_events(browser, team, event_list):
    pass


def create_event_list(browser, team):
    event_list = []
    event_list = add_events(browser, team, event_list)


def record_team_events(browser, season, division, league, team, stats):
    # count_events(browser, team)
    event_list = create_event_list(browser, team)
    # update_team_events(team, event_list)
    # report_teams(league, team)
    # return record_events(browser, season, division, league, team, stats)