from actions.frame_handling import switch_to_page_frame
from classes.Team import Team
from actions.pages import get_page_data, get_page_handler
from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link, script_execution
from variables.general import row_class_name, row_data_tag, link_tag_name
from variables.scripts import next_page_script


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
        team_abbreviation = locate_elements_by_tag_name(row, row_data_tag, "team abbreviation")[2]
        team_links.append({
            "name": link_element.text,
            "link": get_direct_link(link_element),
            "abbreviation": team_abbreviation
            })
    return team_links


def add_page_teams(browser, league, team_list):
    page_data = get_page_data(browser, False)
    team_links = get_team_links(page_data)
    team_list.extend(team_links)
    print(f'Added {str(len(team_links))} teams to "{league.name}" team list.')


def add_teams(browser, league, team_list):
    add_page_teams(browser, league, team_list)
    while len(team_list) < league.number_teams:
        switch_to_page_frame(browser)
        script_execution(browser, next_page_script)
        add_page_teams(browser, league, team_list)
    return team_list


def validate_team_list(browser, league, team_list):
    while league.number_teams != len(team_list):
        print(f'Teams list calculated incorrectly, located '
              f'{str(len(league_list))} teams out of '
              f'{str(league.number_teams)} found in initial count, trying again.')
        league_list = add_teams(browser, league, team_list)
    return league_list


def create_team_list(browser, league):
    team_list = []
    team_list = add_teams(browser, league, team_list)
    return validate_team_list(browser, league, team_list)


def update_league_teams(league, team_list):
    teams = [Team(team["name"], team["link"], team["abbreviation"]) for team in team_list]
    league.teams = teams


def report_teams(division, league):
    print(f'{str(league.number_teams)} teams found for the '
          f'{league.name} {division.name} division.\n')


def check_for_team_results():
    pass


def search_team():
    pass


def record_teams():
    pass


def record_league_teams(browser, season, division, league, stats):
    count_teams(browser, league)
    team_list = create_team_list(browser, league)
    update_league_teams(league, team_list)
    report_teams(division, league)
    # return record_teams()
