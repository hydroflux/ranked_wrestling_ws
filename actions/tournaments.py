from actions.duals import record_event_duals
from actions.matches import record_event_matches
from actions.pages import get_page_data
from classes.Event import Event
from objects.invalid_search import check_for_results, record_invalid_event
from selenium_utilities.locators import locate_element_by_class_name, locate_element_by_tag_name, locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index
from variables.general import row_class_name, row_data_tag, link_tag_name, event_types


def update_event_and_tournament_information(event):
    event.is_tournament = True
    event.tournament_name = event.name
    event.name = ''
    event.tournament_link = event.link
    event.link = ''


def build_tournament_event_link(event, tournament_information):
    link_element = locate_element_by_tag_name(tournament_information[2], link_tag_name, "event link", True)
    tournament_event_link = {
        "name": link_element.text,
        "link": get_direct_link(link_element),
        "date": tournament_information[1].text,
        "time": tournament_information[3].text,
        "level": tournament_information[4].text,
        "tournament_name": event.tournament_name,
        "tournament_link": event.tournament_link
    }
    return tournament_event_link


def get_tournament_event_links(browser, event):
    tournament_links = []
    page_data = get_page_data(browser, False)
    tournament_event_rows = locate_elements_by_class_name(page_data, row_class_name, 'tournament event rows')
    for row in tournament_event_rows:
        tournament_information = locate_elements_by_tag_name(row, row_data_tag, "tournament event information")
        tournament_links.append(build_tournament_event_link(event, tournament_information))
    return tournament_links


def add_page_tournament_events(browser, event, tournament_event_list):
    tournament_links = get_tournament_event_links(browser, event)
    tournament_event_list.extend(tournament_links)
    print(f'Added {str(len(tournament_links))} tournament_events to the "{event.tournament_name}" tournament list.')


def add_tournament_events(browser, event, tournament_event_list):
    add_page_tournament_events(browser, event, tournament_event_list)
    while len(tournament_event_list) < event.number_tournament_events:
        print('Encountered multiple tournament event pages, please review, update code, & re-start.')
        input('Press enter to continue...')
    return tournament_event_list


# validate_tournament_events


def create_tournament_event_list(browser, event):
    tournament_event_list = []
    return add_tournament_events(browser, event, tournament_event_list)


def update_tournament_events(event, tournament_event_list):
    tournament_events = [Event(tournament_event["name"],
                               tournament_event["link"],
                               tournament_event["date"],
                               tournament_event["time"],
                               tournament_event["level"],
                               tournament_name=tournament_event["tournament_name"],
                               tournament_link=tournament_event["tournament_link"]) for tournament_event in tournament_event_list]
    event.tournament_events = tournament_events
    # Below only necessary while 'count_tournament_events' is not a function
    event.number_tournament_events = len(tournament_events)


def report_tournament_events(league, team, event):
    tournament_event_names = [tournament_event.name for tournament_event in event.tournament_events]
    all_tournament_events = iterate_list(tournament_event_names)
    print(f'{str(event.number_tournament_events)} tournament events found for the '
          f'"{event.tournament_name}" tournament for the "{team.name}" team:')
    print_list_by_index(all_tournament_events)


def open_tournament_event(browser, event):
    script_execution(browser, event.link)


def handle_tournament_event_type(browser, division, league, team, event, stats):
    event.type = browser.title
    if event.type == event_types['single_event']:
        record_event_matches(browser, division, league, team, event, stats)
    elif event.type == event_types['dual_event']:
        record_event_duals(browser, division, league, team, event, stats)


def search_tournament_event(browser, division, league, team, event, stats):
    print(f'\nSearching "{event.name}" for matches...')
    open_tournament_event(browser, event)
    if check_for_results(browser):
        handle_tournament_event_type(browser, division, league, team, event, stats)
    else:
        record_invalid_event(browser, division, league, team, event, stats)
    else:
        print(f'Browser encountered an unknown event type of "{event.type}" '
              f'while searching "{event.tournament_name}" event "{event.name}", '
              f'please review...')
        input()
    # close_event_tab(browser)  #  Add a flag in order to aggregate 'tournaments' and 'events' together


def record_tournament_events(browser, division, league, team, event, stats):
    pass


# 'tournaments' have the same general structure as 'events'
def record_tournament(browser, division, league, team, event, stats):
    update_event_and_tournament_information(event)
    tournament_event_list = create_tournament_event_list(browser, event)
    update_tournament_events(event, tournament_event_list)
    # report_tournament_events(league, team, event)
    print('Press enter to continue...')
    input()