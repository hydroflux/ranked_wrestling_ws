from classes.Team import Team

from objects.invalid_search import check_for_results, record_invalid_team

from selenium_utilities.locators import (locate_elements_by_class_name,
                                         locate_elements_by_tag_name)

from settings.general_functions import get_direct_link, script_execution

from variables.general import link_tag_name, row_class_name, row_data_tag
from variables.scripts import next_page_script

from actions.events import record_team_events
from actions.frame_handling import switch_to_page_frame
from actions.pages import get_page_data, get_page_handler


# get_number_leagues & get_number_teams is the EXACT same function
def get_number_teams(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


# very similar to report_number_leagues
def report_number_teams(league):
    print(f'{str(league.number_teams)} total teams located for the '
          f'"{league.name}" League.')


# very similar to count_leagues
def count_teams(browser, league):
    page_handler = get_page_handler(browser, False)
    league.number_teams += get_number_teams(page_handler)
    report_number_teams(league)


# def build_team_link():
#     pass


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
              f'{str(len(team_list))} teams out of '
              f'{str(league.number_teams)} found in initial count, trying again.')
        team_list = add_teams(browser, league, team_list)
    return team_list


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


def search_team(browser, season, division, league, team, stats):
    print(f'Searching "{team.name}" for events...')
    browser.get(team.link)
    if check_for_results(browser):
        record_team_events(browser, season, division, league, team, stats)
    else:
        record_invalid_team(browser, division, league, team, stats)


def record_teams(browser, season, division, league, stats):
    return [search_team(browser, season, division, league, team, stats) for team in league.teams]


def record_league_teams(browser, season, division, league, stats):
    count_teams(browser, league)
    team_list = create_team_list(browser, league)
    update_league_teams(league, team_list)
    report_teams(division, league)
    return record_teams(browser, season, division, league, stats)
