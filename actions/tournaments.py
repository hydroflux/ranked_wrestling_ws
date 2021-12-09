from actions.pages import get_page_data
from selenium_utilities.locators import locate_element_by_class_name, locate_elements_by_class_name, locate_elements_by_tag_name
from variables.general import row_class_name, row_data_tag


def update_event_and_tournament_name(event):
    event.tournament_name = event.name
    event.name = ''


def build_tournament_event_link(browser, tournament_event_information):
    pass


def get_tournament_event_links(browser):
    tournament_links = []
    page_data = get_page_data(browser, False)
    tournament_event_rows = locate_elements_by_class_name(page_data, row_class_name, 'tournament event rows')
    for row in tournament_event_rows:
        tournament_information = locate_elements_by_tag_name(row, row_data_tag)
        tournament_links.append(build_tournament_event_link(browser, tournament_information))
    return tournament_links


def add_page_tournament_events(browser, team, event, tournament_event_list):
    tournament_links = get_tournament_event_links(browser)
    tournament_event_list.extend(tournament_links)
    print(f'Added {str(len(tournament_links))} tournament_events to the "{event.tournament_name}" tournament list.')


def add_tournament_events(browser, team, event, tournament_event_list):
    add_page_tournament_events(browser, team, event, tournament_event_list)
    while len(tournament_event_list) < event.number_tournament_events:
        print('Encountered multiple tournament event pages, please review, update code, & re-start.')
        input('Press enter to continue...')
    return tournament_event_list


# validate_tournament_events


def create_tournament_event_list(browser, team, event):
    tournament_event_list = []
    return add_tournament_events(browser, team, event, tournament_event_list)


def update_tournament_events(team, event, tournament_event_list):
    pass


def report_tournament_events(league, team, event):
    pass


def open_tournament_event(browser, event):
    pass


def search_tournament_event(browser ,division, league, team, event, stats):
    pass


def record_tournament_events(browser, division, league, team, event, stats):
    pass


# 'tournaments' have the same general structure as 'events'
def record_tournament(browser, division, league, team, event, stats):
    update_event_and_tournament_name(event)
    tournament_event_list = create_tournament_event_list(browser, team, event)
    # update_tournament_events(team, event, tournament_event_list)
    # report_tournament_events(league, team, event)
    print('Press enter to continue...')
    input()