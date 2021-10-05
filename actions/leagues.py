from objects.invalid_search import record_invalid_league

from objects.stats import stats

from selenium_utilities.locators import (locate_element_by_class_name,
                                         locate_elements_by_class_name,
                                         locate_elements_by_tag_name)

from settings.general_functions import get_direct_link, script_execution

from variables.general import (league_link_tag_name, league_row_class_name,
                               no_records_class)
from variables.scripts import next_page_script

from actions.cities import record_cities
from actions.pages import get_page_data, get_page_handler


def get_number_leagues(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


def report_number_leagues(division):
    print(f'Total Leagues for the {division.name} Division:\n'
          f'{str(division.number_leagues)}')


def count_leagues(browser, division):
    page_handler = get_page_handler(browser)
    division.number_leagues += get_number_leagues(page_handler)
    report_number_leagues(division)


def get_league_links(page_data):
    league_links = []
    league_rows = locate_elements_by_class_name(page_data, league_row_class_name, 'league rows')
    for row in league_rows:
        link_element = locate_elements_by_tag_name(row, league_link_tag_name, "league link", True)[1]
        league_links.append({"name": link_element.text, "link": get_direct_link(link_element)})
    return league_links


def add_page_leagues(browser, league_list):
    page_data = get_page_data(browser)
    league_links = get_league_links(page_data)
    league_list.extend(league_links)
    print(f'Added {str(len(league_links))} leagues to league links list.')


def add_leagues(browser, division, league_list):
    league_list = []
    add_page_leagues(browser, league_list)
    while len(league_list) < division.number_leagues: 
        script_execution(browser, next_page_script)
        add_page_leagues(browser, league_list)
    return league_list
    

def validate_league_list(browser, division, league_list):
    while division.number_leagues != len(league_list):
        print(f'Leagues list calculated incorrectly, located '
              f'{str(len(league_list))} leagues out of '
              f'{str(division.number_leagues)} found in initial count, trying again.')
        league_list = add_leagues(browser, division)
    return league_list


def create_league_list(browser, division):
    league_list = add_leagues(browser, division)
    return validate_league_list(browser, division, league_list)


def report_leagues(season, division):
    print(f'{str(division.number_leagues)} leagues found for the '
          f'{division.name} {season.title} season.\n')


def check_for_league_results(browser):
    page_data = get_page_data(browser)
    if not locate_element_by_class_name(page_data, no_records_class, "no records"): return True


def search_league(browser, season, division, league, stats):
    print(f'Searching "{league["name"]}" by city...')
    browser.get(league["link"])
    if check_for_league_results(browser):
        record_cities(browser, season, division, league, stats)
    else:
        record_invalid_league(browser, division, league, stats)


def record_leagues(browser, season, division, league_list):
    return [search_league(browser, season, division, league, stats) for league in league_list]


def record_division_leagues(browser, season, division):
    count_leagues(browser, division)
    league_list = create_league_list(browser, division)
    report_leagues(season, division)
    return record_leagues(browser, season, division, league_list)
