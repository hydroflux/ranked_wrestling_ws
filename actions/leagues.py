from settings.general_functions import script_execution

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
    pass


def add_leagues(browser, league_list):
    page_data = get_page_data(browser)
    league_links = get_league_links(page_data)
    league_list.extend(league_links)
    print(f'Added {str(len(league_links))} leagues to league links list.')


def validate_number_leagues(browser, division):
    league_list = []
    add_leagues(browser, league_list)
    return league_list


def create_league_list(browser, season, division):
    count_leagues(browser, division)
    validate_number_leagues(browser, division)
