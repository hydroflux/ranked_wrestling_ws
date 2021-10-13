from actions.pages import get_page_data, get_page_handler
from selenium_utilities.locators import locate_element_by_tag_name, locate_elements_by_class_name, locate_elements_by_tag_name

from settings.general_functions import get_direct_link
from variables.general import row_class_name, link_tag_name, row_data_tag

# def get_number_events(page_handler):
#     handler_text = page_handler.text
#     return int(handler_text[handler_text.rfind(' ') + 1:])


# def report_number_teams(team):
#     print(f'{str(team.number_events)} total events located for the '
#           f'"{team.name}" Team.')


# def count_events(browser, team):
#     page_handler = get_page_handler(browser)


def build_event_link(event_information):
    link_element = locate_element_by_tag_name(event_information[2], link_tag_name, "event link", True)
    event_link = {
        "name": link_element.text,
        "link": get_direct_link(link_element),
        "date": event_information[1].text,
        "time": event_information[3].text,
        "level": event_information[4].text
    }
    return event_link


def get_event_links(page_data):
    event_links = []
    event_rows = locate_elements_by_class_name(page_data, row_class_name, 'event rows')
    for row in event_rows:
        event_information = locate_elements_by_tag_name(row, row_data_tag, "event information")
        event_links.append(build_event_link(event_information))
    return event_links


def add_page_events(browser, team, event_list):
    page_data = get_page_data(browser, False)
    event_links = get_event_links(page_data)
    event_list.extend(event_links)
    print(f'Added {str(len(event_links))} events to "{team.name}" team list.')


def add_events(browser, team, event_list):
    add_page_events(browser, team, event_list)
    while len(event_list) < team.number_events:
        print('Encountered multiple event pages, please review, update code, & re-start.')
        input()
    return event_list


def create_event_list(browser, team):
    event_list = []
    event_list = add_events(browser, team, event_list)


def record_team_events(browser, season, division, league, team, stats):
    # count_events(browser, team)
    event_list = create_event_list(browser, team)
    # update_team_events(team, event_list)
    # report_teams(league, team)
    # return record_events(browser, season, division, league, team, stats)