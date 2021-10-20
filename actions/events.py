from classes.Event import Event

from objects.invalid_search import check_for_results, record_invalid_event

from selenium_utilities.locators import (locate_element_by_tag_name,
                                         locate_elements_by_class_name,
                                         locate_elements_by_tag_name)
from selenium_utilities.window_handler import close_event_tab, switch_to_event_tab

from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index

from variables.general import link_tag_name, row_class_name, row_data_tag, event_types

from actions.matches import record_event_matches
from actions.pages import get_page_data, get_page_handler


def build_event_link(browser, event_information):
    link_element = locate_element_by_tag_name(event_information[2], link_tag_name, "event link", True)
    event_link = {
        "name": link_element.text,
        "link": get_direct_link(link_element),
        "date": event_information[1].text,
        "time": event_information[3].text,
        "level": event_information[4].text,
    }
    return event_link


def get_event_links(browser):
    event_links = []
    page_data = get_page_data(browser, False)
    event_rows = locate_elements_by_class_name(page_data, row_class_name, 'event rows')
    for row in event_rows:
        event_information = locate_elements_by_tag_name(row, row_data_tag, "event information")
        event_links.append(build_event_link(browser, event_information))
    return event_links


def add_page_events(browser, team, event_list):
    event_links = get_event_links(browser)
    event_list.extend(event_links)
    print(f'Added {str(len(event_links))} events to "{team.name}" team list.')


def add_events(browser, team, event_list):
    add_page_events(browser, team, event_list)
    while len(event_list) < team.number_events:
        print('Encountered multiple event pages, please review, update code, & re-start.')
        input('Press enter to continue...')
    return event_list


# validate_event_list


def create_event_list(browser, team):
    event_list = []
    return add_events(browser, team, event_list)


def update_team_events(team, event_list):
    events = [Event(event["name"],
                    event["link"],
                    event["date"],
                    event["time"],
                    event["level"]) for event in event_list]
    team.events = events
    # Below only necessary while 'count_events' is not a function
    team.number_events = len(events)


def report_events(league, team):
    event_names = [event.name for event in team.events]
    all_events = iterate_list(event_names)
    print(f'{str(team.number_events)} events found for the '
          f'{team.name} {league.name} league:')
    print_list_by_index(all_events)
    

def open_event(browser, event):
    script_execution(browser, event.link)
    switch_to_event_tab(browser)


def handle_event_type(browser, season, division, league, team, event, stats):
    event.type = browser.title
    if event.type == event_types['single_event']:
        record_event_matches(browser, season, division, league, team, event, stats)
    elif event.type == event_types['dual_event']:
        pass
    elif event.type == event_types['tournament']:
        pass
    else:
        print(f'Browser encountered an unknown event type of "{event.type}", please review...')
        input()


def search_event(browser, season, division, league, team, event, stats):
    print(f'\nSearching "{event.name}" for matches...')
    open_event(browser, event)
    handle_event_type(browser, season, division, league, team, event, stats)
    if check_for_results(browser):
        handle_event_type(browser, season, division, league, team, event, stats)
    else:
        record_invalid_event(browser, division, league, team, event, stats)
    close_event_tab(browser)


def record_events(browser, season, division, league, team, stats):
    return [search_event(browser, season, division, league, team, event, stats) for event in team.events]


def record_team_events(browser, season, division, league, team, stats):
    # count_events(browser, team)
    event_list = create_event_list(browser, team)
    update_team_events(team, event_list)
    report_events(league, team)
    return record_events(browser, season, division, league, team, stats)
