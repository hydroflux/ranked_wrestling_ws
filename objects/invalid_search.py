from classes.Stat import Stat
from actions.pages import get_page_data
from selenium_utilities.locators import locate_element_by_class_name
from variables.general import no_records_class


def check_for_results(browser):
    page_data = get_page_data(browser, False)
    if not locate_element_by_class_name(page_data, no_records_class, "no records", quick=True): return True


def record_invalid_league(browser, division, league, stats):
    stat = Stat(
        state=division.state,
        division_name=division.name,
        division_abbreviation=division.division_abbreviation,
        number_leagues=division.number_leagues,
        league_name=league.name,
        league_link=league.link,
        number_teams=league.number_teams,
        team_name='N/A',
        team_link='N/A',
        team_abbreviation='N/A',
        number_events='N/A',
        event_name='N/A',
        date='N/A',
        time='N/A',
        level='N/A',
        type='N/A',
        number_matches='N/A',
        weight='N/A',
        summary='N/A',
        stat_flag='N/A',
        tw_event='N/A',
        match_level='N/A',
        round='N/A',
        winning_team='N/A',
        winner='N/A',
        losing_team='N/A',
        loser='N/A',
        result='N/A',
        match_time='N/A',
        winning_point='N/A',
        losing_point='N/A',
    )
    stats.append(stat)


def record_invalid_team(browser, division, league, team, stats):
    stat = Stat(
        state=division.state,
        division_name=division.name,
        division_abbreviation=division.division_abbreviation,
        number_leagues=division.number_leagues,
        league_name=league.name,
        league_link=league.link,
        number_teams=league.number_teams,
        team_name=team.name,
        team_link=team.link,
        team_abbreviation=team.abbreviation,
        number_events=team.number_events,
        event_name='N/A',
        date='N/A',
        time='N/A',
        level='N/A',
        type='N/A',
        number_matches='N/A',
        weight='N/A',
        summary='N/A',
        stat_flag='N/A',
        tw_event='N/A',
        match_level='N/A',
        round='N/A',
        winning_team='N/A',
        winner='N/A',
        losing_team='N/A',
        loser='N/A',
        result='N/A',
        match_time='N/A',
        winning_point='N/A',
        losing_point='N/A',
    )
    stats.append(stat)


def record_invalid_event(browser, division, league, team, event, stats):
    stat = Stat(
        state=division.state,
        division_name=division.name,
        division_abbreviation=division.division_abbreviation,
        number_leagues=division.number_leagues,
        league_name=league.name,
        league_link=league.link,
        number_teams=league.number_teams,
        team_name=team.name,
        team_link=team.link,
        team_abbreviation=team.abbreviation,
        number_events=team.number_events,
        event_name=event.name,
        date=event.date,
        time=event.time,
        level=event.level,
        type=event.type,
        number_matches=event.number_matches,
        weight='N/A',
        summary='N/A',
        stat_flag='N/A',
        tw_event='N/A',
        match_level='N/A',
        round='N/A',
        winning_team='N/A',
        winner='N/A',
        losing_team='N/A',
        loser='N/A',
        result='N/A',
        match_time='N/A',
        winning_point='N/A',
        losing_point='N/A',
    )
    stats.append(stat)
