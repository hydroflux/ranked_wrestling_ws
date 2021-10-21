from classes.League import League

from objects.invalid_search import check_for_results, record_invalid_league

from selenium_utilities.locators import (locate_elements_by_class_name,
                                         locate_elements_by_tag_name)

from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index

from variables.general import link_tag_name, row_class_name
from variables.scripts import next_page_script

from actions.pages import get_page_data, get_page_handler
from actions.teams import record_league_teams


# get_number_leagues & get_number_teams is the EXACT same function
def get_number_leagues(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


def report_number_leagues(division):
    print(f'{str(division.number_leagues)} total leagues located for the '
          f'"{division.name}" Division.')


def count_leagues(browser, division):
    page_handler = get_page_handler(browser)
    division.number_leagues += get_number_leagues(page_handler)
    report_number_leagues(division)


# def build_league_link():
#     pass


def get_league_links(browser):
    league_links = []
    page_data = get_page_data(browser)
    league_rows = locate_elements_by_class_name(page_data, row_class_name, 'league rows')
    for row in league_rows:
        link_element = locate_elements_by_tag_name(row, link_tag_name, "league link", True)[1]
        league_links.append({"name": link_element.text, "link": get_direct_link(link_element)})
    return league_links


def add_page_leagues(browser, division, league_list):
    league_links = get_league_links(browser)
    league_list.extend(league_links)
    print(f'Added {str(len(league_links))} leagues to "{division.name}" leagues list.')


def add_leagues(browser, division, league_list):
    add_page_leagues(browser, division, league_list)
    while len(league_list) < division.number_leagues: 
        script_execution(browser, next_page_script)
        add_page_leagues(browser, division, league_list)
    return league_list
    

def validate_league_list(browser, division, league_list):
    while division.number_leagues != len(league_list):
        print(f'Leagues list calculated incorrectly, located '
              f'{str(len(league_list))} leagues out of '
              f'{str(division.number_leagues)} found in initial count, trying again.')
        league_list = add_leagues(browser, division, league_list)
    return league_list


def create_league_list(browser, division):
    league_list = []
    league_list = add_leagues(browser, division, league_list)
    return validate_league_list(browser, division, league_list)


def update_division_leagues(division, league_list):
    leagues = [League(league["name"], league["link"]) for league in league_list]
    division.leagues = leagues



def report_leagues(season, division):
    league_names = [league.name for league in division.leagues]
    all_leagues = iterate_list(league_names)
    print(f'{str(division.number_leagues)} leagues found for the '
          f'{division.name} {season.title} season:')
    print_list_by_index(all_leagues)
          


def search_league(browser, division, league, stats):
    print(f'\nSearching "{league.name}" for teams...')
    browser.get(league.link)
    if check_for_results(browser):
        record_league_teams(browser, division, league, stats)
    else:
        record_invalid_league(browser, division, league, stats)


def record_leagues(browser, division, stats):
    # return [search_league(browser, division, league, stats) for league in division.leagues]
    return [search_league(browser, division, league, stats) for league in division.leagues[-1:]]  # testing


def record_division_leagues(browser, season, division):
    stats = []
    count_leagues(browser, division)
    league_list = create_league_list(browser, division)
    update_division_leagues(division, league_list)
    report_leagues(season, division)
    stats = record_leagues(browser, division, stats)
    return stats
