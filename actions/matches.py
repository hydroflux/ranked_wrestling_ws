from classes.Match import Match
from classes.Stat import Stat
from actions.pages import get_page_data
from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index

from variables.general import row_class_name, row_data_tag
from variables.matches import level_values, summary_flags, round_flag, unknown_values, participant_flags, result_options


def handle_event_level(match, match_summary):
    if match_summary.startswith(level_values["level_1_tag"]):
        match.level = level_values["level_1_value"]
        match_summary = match_summary[10:]
    elif match_summary.startswith(level_values["level_2_tag"]):
        match.level = level_values["level_2_value"]
        match_summary = match_summary[17:]
    elif match_summary.startswith(level_values["level_3_tag"]):
        match.level = level_values["level_3_value"]
        match_summary = match_summary[16:]
    elif match_summary.startswith(level_values["level_4_tag"]):
        match.level = level_values["level_4_value"]
        match_summary = match_summary[12:]
    return match_summary


def check_for_round_flag(match, summary, option=None):
    if round_flag in summary:
        match.round = summary[: summary.index(round_flag)]
        if option is not None:
            return summary[(len(match.round) + 3):]
    else:
        return summary


def handle_unknown_values(match, option=None):
    unknown = unknown_values[0]
    if option is None:
        match.winner = unknown
        match.winning_team = unknown
        match.loser = unknown
        match.losing_team = unknown
    elif option == 'winning summary':
        match.winner = unknown
        match.winning_team = unknown
    elif option == 'losing summary':
        match.loser = unknown
        match.losing_team = unknown


def handle_match_point(match):
    if match.point is not None:
        match.winning_point, match.losing_point = match.point.split('-')


def split_match_result(match, result):
    if result.startswith(result_options['flag_1']):
        match.result = result_options["value_1"]
        match.point = result[4:]
    elif result == result_options['flag_2']:
        match.result = result_options['value_2']
    elif result == result_options['flag_3']:
        match.result = result_options['value_3']
    elif result.startswith(result_options['flag_4']):
        match.result = result_options['value_4']
        match.time = result[5:]
    elif result == result_options['flag_5']:
        match.result = result_options['value_5']
    elif result == result_options['flag_6']:
        match.result = result_options['value_6']
    elif result == result_options['flag_7']:
        match.result = result_options['value_7']
    elif result.startswith(result_options['flag_8']):
        match.result = result_options['value_8']
        match.point = result[3:]
    elif result == result_options['flag_9']:
        match.result = result_options['value_9']
    elif result.startswith(result_options['flag_10']):
        if result.startswith(result_options['flag_11']):
            match.result = result_options['value_11']
            match.time = result[12:]
        else:
            match.result = result_options['value_10']
            match.point = result[5:]
    elif result.startswith('flag_12'):
        if result.startswith(result_options['flag_13']):
            match.result = result_options['value_13']
            match.time = result[12:]
        else:
            match.result = result_options['value_12']
            match.point = result[5:]
    elif result.startswith(result_options['flag_14']):
        match.result = result_options['value_14']
        match.time = result[(result.rfind(' ') + 1):]
        match.point = result[3: result.rfind(' ')]
    elif result.startswith(result_options['flag_15']):
        match.result = result_options['value_15']
        match.point = result[4:]
    else:
        match.result = result
    handle_match_point(match)


def handle_event_participants(match, summary):
    if summary_flags['flag_1'] in summary:
        winning_summary, losing_summary = summary.split(summary_flags['flag_1'])
        if round_flag in winning_summary:
            match.round = winning_summary[:winning_summary.index(round_flag)]
            winning_summary = winning_summary[(len(match.round) + 3):]
        if winning_summary in unknown_values:
            handle_unknown_values(match, 'winning summary')
        else:
            match.winner = winning_summary[:(winning_summary.find(participant_flags['1']) - 1)]
            match.winning_team = winning_summary[(winning_summary.find(participant_flags['1']) + 1): -1]
        if losing_summary in unknown_values:
            handle_unknown_values(match, 'losing summary')
        else:
            match.loser = losing_summary[:(losing_summary.find(participant_flags['1']) - 1)]
            match.losing_team = losing_summary[(losing_summary.find(participant_flags['1']) + 1): -1]
    elif summary.endswith(summary_flags['flag_2']):
        check_for_round_flag(match, summary)
        handle_unknown_values(match)
        match.result = summary_flags['flag_2']
    elif summary.endswith(summary_flags['flag_3']):
        check_for_round_flag(match, summary)
        handle_unknown_values(match)
        match.result = summary_flags['flag_3']
    elif summary_flags['flag_4'] in summary:
        check_for_round_flag(match, summary)
        handle_unknown_values(match)
        if participant_flags['1'] in summary:
            result = summary[(summary.find(participant_flags['1']) + 1): -1]
            split_match_result(match, result)
    elif summary_flags['flag_5'] in summary:
        winning_summary = summary[:summary.find(summary_flags['flag_5'])]
        updated_winning_summary = check_for_round_flag(match, winning_summary, option='return')
        if updated_winning_summary in unknown_values:
            handle_unknown_values(match, 'winning summary')
        else:
            match.winner = updated_winning_summary[:updated_winning_summary.find(f' {participant_flags["1"]}')]
            if participant_flags["3"] in updated_winning_summary:
                match.winning_team = updated_winning_summary[(updated_winning_summary.find(participant_flags["1"]) + 1):(updated_winning_summary.find(participant_flags["3"]) + 1)]
            elif participant_flags["2"] in updated_winning_summary:
                match.winning_team = updated_winning_summary[(updated_winning_summary.find(participant_flags["1"]) + 1):updated_winning_summary.find(participant_flags["2"])]
            losing_summary = summary[(summary.find(summary_flags['flag_5']) + 6):]
            if participant_flags["4"] in losing_summary:
                end_index = losing_summary.rfind(participant_flags['4']) + 3
            elif participant_flags["5"] in losing_summary:
                end_index = losing_summary.rfind(participant_flags['5']) + 2
            match.result = losing_summary[end_index: -1]
            updated_losing_summary = losing_summary[: end_index]
            if updated_losing_summary in unknown_values:
                handle_unknown_values(match, 'losing summary')
            elif participant_flags["1"] in updated_losing_summary:
                losing_index = updated_losing_summary.rfind(participant_flags["1"])
                if updated_losing_summary.endswith(participant_flags["2"]) or updated_losing_summary.endswith(participant_flags["6"]):
                    losing_index = (updated_losing_summary[:losing_index]).rfind(participant_flags["1"])
                match.loser = updated_losing_summary[: (losing_index - 1)]
                match.losing_team = updated_losing_summary[(losing_index + 1):]
        split_match_result(match, match.result)
    elif summary.endswith(summary_flags['flag_6']):
        winning_summary = summary[:summary.find(summary_flags['flag_6'])]
        updated_winning_summary = check_for_round_flag(match, winning_summary, option='return')
        match.winner = winning_summary[:winning_summary.find(participant_flags['5'])]
        if participant_flags['3'] in winning_summary:
            match.winning_team = winning_summary[(winning_summary.find(participant_flags['1']) + 1): winning_summary.find(participant_flags['3'])]
        elif participant_flags['2'] in winning_summary:
            match.winning_team = winning_summary[(winning_summary.find(participant_flags['1']) + 1): winning_summary.find(participant_flags['2'])]
        handle_unknown_values(match, 'losing summary')
        match.result = result_options["value_16"]


def split_match_summary_information(match, match_summary):
    summary = handle_event_level(match, match_summary)
    handle_event_participants(match, summary)


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


def get_match_summary_information(browser):
    match_summary_information = []
    page_data = get_page_data(browser, False)
    match_rows = locate_elements_by_class_name(page_data, row_class_name, 'match rows')
    for row in match_rows:
        match_information = locate_elements_by_tag_name(row, row_data_tag, "match information")
        match_summary_information.append(build_single_match_information(match_information))
    return match_summary_information


def add_page_matches(browser, event, match_list):
    match_summary_information = get_match_summary_information(browser)
    match_list.extend(match_summary_information)
    print(f'Added {str(len(match_summary_information))} events to "{event.name}" team list.')


def add_matches(browser, event, match_list):
    add_page_matches(browser, event, match_list)
    while len(match_list) < event.number_matches:
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
    print(f'{str(event.number_matches)} matches found for the '
          f'"{event.name}" for "{team.name}":')
    print_list_by_index(all_matches)


def record_stat(season, division, league, team, event, match, stats):
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
        weight=match.weight,
        summary=match.summary,
        stat_flag=match.stat_flag,
        tw_event=match.tw_event,
        match_level=match.level,
        round=match.round,
        winning_team= match.winning_team,
        winner=match.winner,
        losing_team=match.losing_team,
        loser=match.loser,
        results=match.results,
        match_time=match.match_time,
        winning_point=match.winning_point,
        losing_point=match.losing_point,
    )
    stats.append(stat)


def record_match_list(season, division, league, team, event, match_list, stats):
    for match in match_list:
        record_stat(season, division, league, team, event, match, stats)


def record_event_matches(browser, season, division, league, team, event, stats):
    match_list = create_match_list(browser, event)
    update_event_matches(event, match_list)
    report_matches(team, event)
    record_match_list(season, division, league, team, event, match_list, stats)