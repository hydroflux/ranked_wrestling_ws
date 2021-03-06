from time import sleep

from classes.Match import Match
from classes.Stat import Stat

from selenium_utilities.locators import (locate_elements_by_class_name,
                                         locate_elements_by_tag_name)

from settings.printer import iterate_list, print_list_by_index

from variables.general import row_class_name, row_data_tag

from actions.match_types import handle_match_types
from actions.pages import get_page_data
from actions.summary_breakdown import handle_event_level


def split_match_summary_information(match, match_summary):
    summary = handle_event_level(match, match_summary)
    handle_match_types(match, summary)


def build_single_match_information(match_information):
    match_summary = match_information[2].text 
    match = Match(
        weight=match_information[1].text,
        summary=match_summary,
        stat_flag=match_information[3].text,
        tw_event=match_information[4].text,
    )
    split_match_summary_information(match, match_summary)
    return match


# Nearly identical to similar 'duals' script function
def get_match_rows(browser):
    page_data = get_page_data(browser, False)
    return locate_elements_by_class_name(page_data, row_class_name, 'match rows')


# Nearly identical to similar 'duals' script function
def access_match_rows(browser):
    match_rows = get_match_rows(browser)
    while match_rows is None:
        print('Returned "NoneType" for match rows, refreshing & trying again...')
        browser.refresh()
        sleep(10)
        match_rows = get_match_rows(browser)
    return match_rows


def get_match_summary_information(browser):
    match_summary_information = []
    match_rows = access_match_rows(browser)
    for row in match_rows:
        match_information = locate_elements_by_tag_name(row, row_data_tag, "match information")
        match_summary_information.append(build_single_match_information(match_information))
    return match_summary_information


def add_page_matches(browser, event, match_list):
    match_summary_information = get_match_summary_information(browser)
    match_list.extend(match_summary_information)
    print(f'Added {str(len(match_summary_information))} matches to "{event.name}" event list.')


def add_matches(browser, event, match_list):
    add_page_matches(browser, event, match_list)
    while len(match_list) < event.number_matches:  # Currently irrelevant, need to update in order to capture number_matches
        print('Encountered multiple match pages, please review, update code, & re-start')
        input('Press enter to continue...')
    return match_list


def create_match_list(browser, event):
    match_list = []
    return add_matches(browser, event, match_list)


def update_event_matches(event, match_list):
    event.matches = match_list
    event.number_matches = len(match_list)


def report_matches(team, event):
    match_summaries = [match.summary for match in event.matches]
    all_matches = iterate_list(match_summaries)
    if event.is_tournament:
        print(f'{str(event.number_matches)} matches found for the '
              f'"{event.name}" event for the "{event.tournament_name}" tournament for team'
              f'"{team.name}" team:')
    else:
        print(f'{str(event.number_matches)} matches found for the '
              f'"{event.name}" event for the "{team.name}" team:')
    print_list_by_index(all_matches)


def record_stat(division, league, team, event, match, stats):
    stat = Stat(
        state=division.state,
        division_name=division.name,
        division_abbreviation=division.division_abbreviation,
        number_leagues=division.number_leagues,
        league_name=league.name,
        number_teams=league.number_teams,
        team_name=team.name,
        team_abbreviation=team.abbreviation,
        number_events=team.number_events,
        event_name=event.name,
        date=event.date,
        time=event.time,
        level=event.level,
        type=event.type,
        number_matches=event.number_matches,
        weight=match.weight,
        summary=match.summary,
        # Single Match Exclusive
        stat_flag=match.stat_flag,
        tw_event=match.tw_event,
        # Tournament
        is_tournament=event.is_tournament,
        tournament_name=event.tournament_name,
        tournament_winner=event.tournament_winner,
        tournament_runner_up=event.tournament_runner_up,
        # Dual Event Exclusive
        official=event.official,
        comment=event.comment,
        team_one=event.team_one,
        team_one_score=event.team_one_score,
        team_two=event.team_two,
        team_two_score=event.team_two_score,
        # Dual Match Exclusive
        team_one_point=match.team_one_point,
        team_two_point=match.team_two_point,
        # Match Summary Breakdown
        match_level=match.level,
        round=match.round,
        winning_team= match.winning_team,
        winner=match.winner,
        losing_team=match.losing_team,
        loser=match.loser,
        result=match.result,
        match_time=match.time,
        winning_point=match.winning_point,
        losing_point=match.losing_point,
        # Other
        # league_link=league.link,
        # team_link=team.link
    )
    stats.append(stat)


def record_match_list(division, league, team, event, match_list, stats):
    for match in match_list:
        record_stat(division, league, team, event, match, stats)


def record_event_matches(browser, division, league, team, event, stats):
    match_list = create_match_list(browser, event)
    update_event_matches(event, match_list)
    report_matches(team, event)
    return record_match_list(division, league, team, event, match_list, stats)
