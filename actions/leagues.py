from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link, script_execution

from variables.general import league_row_class_name, league_link_tag_name
from variables.scripts import next_page_script

from actions.pages import get_page_data, get_page_handler


def get_number_leagues(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


def report_number_leagues(division):
    print(f'Total Leagues for the {division.name} Division:\n'
          f'{division.number_leagues}')


def count_leagues(browser, division):
    page_handler = get_page_handler(browser)
    division.number_leagues += get_number_leagues(page_handler)
    report_number_leagues(division)


def get_league_links(page_data):
    league_links = []
    league_rows = locate_elements_by_class_name(page_data, league_row_class_name, 'league rows')
    for row in league_rows:
        link_element = locate_elements_by_tag_name(row, league_link_tag_name, "league link", True)[1]
        league_links.append(get_direct_link(link_element))
    return league_links


def add_leagues(browser, league_list):
    page_data = get_page_data(browser)
    league_links = get_league_links(page_data)
    league_list.extend(league_links)
    print(f'Added {str(len(league_links))} leagues to league links list.')


def create_league_list(browser, division):
    league_list = []
    add_leagues(browser, league_list)
    while len(league_list) < division.number_leagues: 
        script_execution(browser, next_page_script)
        add_leagues(browser, league_list)
    return league_list


def record_division_leagues(browser, season, division):
    count_leagues(browser, division)
    league_list = create_league_list(browser, division)
