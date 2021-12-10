from time import sleep

from actions.matches import record_stat, split_match_summary_information, update_event_matches
from classes.Match import Match

from selenium_utilities.locators import (locate_element_by_tag_name, locate_elements_by_class_name,
                                         locate_elements_by_tag_name)
from settings.printer import iterate_list, print_list_by_index

from variables.duals import official_tag, teams_tag, score_tag
from variables.general import row_class_name, row_data_tag

from actions.pages import get_page_data


def build_dual_match_information(match_information):
    match_summary = match_information[2].text 
    match = Match(
        weight=match_information[1].text,
        summary=match_summary,
        team_one_point=match_information[3].text,
        team_two_point=match_information[4].text,
    )
    split_match_summary_information(match, match_summary)
    return match


def determine_dual_results(event):
    if int(event.team_one_score) > int(event.team_two_score):
        event.tournament_winner = event.team_one
        event.tournament_runner_up = event.team_two
    elif int(event.team_one_score) < int(event.team_two_score):
        event.tournament_winner = event.team_two
        event.tournament_runner_up = event.team_one
    elif int(event.team_one_score) == int(event.team_two_score):
        event.tournament_winner = 'Tie'
        event.tournament_runner_up = 'Tie'
    else:
        print(f'Unexpected tournament results for '
              f'"{print(event)}", please review & then press enter...')
        input()


# Nearly identical to similar 'matches' script function
def get_dual_match_rows(browser):
    page_data = get_page_data(browser, False)
    return locate_elements_by_class_name(page_data, row_class_name, 'dual match rows')


# Nearly identical to similar 'matches' script function
def access_dual_match_rows(browser):
    match_rows = get_dual_match_rows(browser)
    while match_rows is None:
        print('Returned "NoneType" for dual match rows, refreshing & trying again...')
        browser.refresh()
        sleep(10)
        match_rows = get_dual_match_rows(browser)
    return match_rows


def breakdown_dual_match_information(event, match_rows):
    while locate_element_by_tag_name(match_rows[-1], row_data_tag, 'dual event last row data').text != '':
        row_text = match_rows[-1].text
        if row_text.startswith(official_tag):
            event.official = row_text[10:]
        elif row_text.startswith(teams_tag):
            _, team_one, team_two = row_text.splitlines()
            event.team_one = team_one.strip()
            event.team_two = team_two.strip()
        elif row_text.startswith(score_tag):
            _, team_one_score, team_two_score = row_text.splitlines()
            event.team_one_score = team_one_score.strip()
            event.team_two_score = team_two_score.strip()
            determine_dual_results(event)
        else:
            event.comment = row_text.strip()
            print('Event Comment:', row_text[-1])
        match_rows.pop()
    return match_rows


def get_dual_summary_information(browser, event):
    dual_summary_information = []
    match_rows = access_dual_match_rows(browser)
    updated_match_rows = breakdown_dual_match_information(event, match_rows)
    for row in updated_match_rows:
        match_information = locate_elements_by_tag_name(row, row_data_tag, 'dual match information')
        dual_summary_information.append(build_dual_match_information(match_information))
    return dual_summary_information


def add_page_dual_matches(browser, event, match_list):
    dual_summary_information = get_dual_summary_information(browser, event)
    match_list.extend(dual_summary_information)
    print(f'Added {str(len(dual_summary_information))} dual matches to "{event.name}" event list.')


# nearly identical to 'add_matches' in the 'matches' script
def add_dual_matches(browser, event, match_list):
    add_page_dual_matches(browser, event, match_list)
    while len(match_list) < event.number_matches:  # Currently irrelevant, need to update in order to capture number_matches
        print('Encountered multiple dual match pages, please review, update code, & re-start')
        input('Press enter to continue...')
    return match_list


def create_dual_match_list(browser, event):
    match_list = []
    return add_dual_matches(browser, event, match_list)


# nearly identical to 'report_matches' in the 'matches' script
def report_duals(team, event):
    dual_match_summaries = [dual_match.summary for dual_match in event.matches]
    all_dual_matches = iterate_list(dual_match_summaries)
    print(f'{str(event.number_matches)} dual matches found for the '
        f'"{event.name}" event for the "{team.name}" team:')
    print_list_by_index(all_dual_matches)


def record_duals_match_list(division, league, team, event, dual_match_list, stats):
    for match in dual_match_list:
        record_stat(division, league, team, event, match, stats)


def record_event_duals(browser, division, league, team, event, stats):
    dual_match_list = create_dual_match_list(browser, event)
    update_event_matches(event, dual_match_list)
    report_duals(team, event)
    return record_duals_match_list(division, league, team, event, dual_match_list, stats)
    
