from actions.matches import split_match_summary_information
from classes.Match import Match
from classes.Stat import Stat

from selenium_utilities.locators import (locate_element_by_tag_name, locate_elements_by_class_name,
                                         locate_elements_by_tag_name)

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


def breakdown_dual_match_information(match, match_rows):
    while locate_element_by_tag_name(match_rows[-1], row_data_tag, "last row data").text != '':
        row_text = match_rows[-1].text
        if row_text.startswith(official_tag):
            match.official = row_text[10:]
        elif row_text.startswith(teams_tag):
            _, team_one, team_two = row_text.splitlines()
            match.team_one = team_one.strip()
            match.team_two = team_two.strip()
        elif row_text.startswith(score_tag):
            match.team_one_score = event_results[-1][1]
            match.team_two_score = event_results[-1][2]
        else:
            match.comment = event_results[-1]
            print(event_results[-1])
        event_results = event_results[:-1]
        match_rows.pop()


def get_dual_summary_information(browser):
    dual_summary_information = []
    page_data = get_page_data(browser, False)
    match_rows = locate_elements_by_class_name(page_data, row_class_name, 'dual match rows')
    updated_match_rows = breakdown_dual_match_information(match, match_rows)
    for row in match_rows:
        match_information = locate_elements_by_tag_name(row, row_data_tag, 'dual match information')
        dual_summary_information.append(build_dual_match_information(match_information))
    return dual_summary_information


def add_page_dual_matches(browser, event, match_list):
    dual_summary_information = get_dual_summary_information(browser)
    match_list.extend(dual_summary_information)
    print(f'Added {str(len(dual_summary_information))} dual matches to "{event.name}" event list.')


# nearly identical to 'add_matches' in the 'matches' script
def add_dual_matches(browser, event, match_list):
    add_page_dual_matches(browser, event, match_list)
    while len(match_list) < event.number_matches:  # Currently irrelevant, need to update in order to capture number_matches
        print('Encountered multiple match pages, please review, update code, & re-start')
        input('Press enter to continue...')
    return match_list


def create_dual_match_list(browser, event):
    match_list = []
    return add_dual_matches(browser, event, match_list)


def update_team_events():  # ?????
    pass


def report_duals():
    pass


def open_event():
    pass


def search_event():
    pass


def record_duals():
    pass


def record_event_duals(browser, division, league, team, event, stats):
    pass
    # match_list = create_dual_match_list(browser, event)
