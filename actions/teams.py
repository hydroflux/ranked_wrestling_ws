from actions.pages import get_page_data, get_page_handler
from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link
from variables.general import row_class_name, link_tag_name


# get_number_leagues & get_number_teams is the EXACT same function
def get_number_teams(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


# very similar to report_number_leagues
def report_number_teams(league):
    print(f'Total Teams for the "{league.name}" League:\n'
          f'{str(league.number_teams)}')


# very similar to count_leagues
def count_teams(browser, league):
    page_handler = get_page_handler(browser, False)
    league.number_teams += get_number_teams(page_handler)
    report_number_teams(league)


# very similar to 'get_league_links'
def get_team_links(page_data):
    team_links = []
    team_rows = locate_elements_by_class_name(page_data, row_class_name, 'team rows')
    for row in team_rows:
        link_element = locate_elements_by_tag_name(row, link_tag_name, "team link", True)[1]
        team_links.append({"name": link_element.text, "link": get_direct_link(link_element)})
    return team_links


def add_page_teams(browser, league, team_list):
    page_data = get_page_data(browser, False)
    team_links = get_team_links(page_data)
    team_list.extend(team_links)
    print(f'Added {str(len(team_links))} teams to "{league.name}" team list.')


def add_teams(browser, league, team_list):
    add_page_teams(browser, league, team_list)


def validate_team_list():
    pass


def create_team_list(browser, league):
    team_list = []
    team_list = add_teams(browser, league, team_list)


def update_league_teams():
    pass


def report_teams():
    pass


def check_for_team_results():
    pass


def search_team():
    pass


def record_teams():
    pass


def record_league_teams(browser, season, division, league, stats):
    count_teams(browser, league)
    team_list = create_team_list(browser, league)
