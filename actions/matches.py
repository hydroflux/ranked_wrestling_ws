from classes.Match import Match
from actions.pages import get_page_data
from selenium_utilities.locators import locate_elements_by_class_name, locate_elements_by_tag_name
from settings.general_functions import get_direct_link, script_execution
from settings.printer import iterate_list, print_list_by_index

from variables.general import row_class_name, row_data_tag
from variables.matches import level_values, summary_flags, round_flag, unknown_values, participant_flags


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


def handle_event_participants(match, summary):
    if summary_flags["flag_1"] in summary:
        winning_summary, losing_summary = summary.split(summary_flags["flag_1"])
        if round_flag in winning_summary:
            match.round = winning_summary[:winning_summary.index(round_flag)]
            winning_summary = winning_summary[(len(match.round) + 3):]
        if winning_summary in unknown_values:
            handle_unknown_values(match, 'winning summary')
        else:
            match.winner = winning_summary[:(winning_summary.find(participant_flags["1"]) - 1)]
            match.winning_team = winning_summary[(winning_summary.find(participant_flags["1"]) + 1): -1]
        if losing_summary in unknown_values:
            handle_unknown_values(match, 'losing summary')
        else:
            match.loser = losing_summary[:(losing_summary.find(participant_flags["1"]) - 1)]
            match.losing_team = losing_summary[(losing_summary.find(participant_flags["1"]) + 1): -1]
    elif summary.endswith(summary_flags["flag_2"]):
        if round_flag in summary:
            match.round = summary[: summary.index(round_flag)]
        handle_unknown_values(match)
        match.result = summary_flags["flag_2"]
    elif summary.endswith(summary_flags["flag_3"]):
        if round_flag in summary:
            match.round = summary[: summary.index(round_flag)]
        handle_unknown_values(match)
        match.result = summary_flags["flag_3"]
    elif summary_flags["flag_4"] in summary:
        pass
    elif summary_flags["flag_5"] in summary:
        pass
    elif summary.endswith(summary_flags["flag_6"]):
        pass


def split_match_summary_information(match, match_summary):
    summary = handle_event_level(match, match_summary)
    handle_event_participants(match, summary)
    pass
    # "rounds": '',
    # "winning_team": '',
    # "winner": '',
    # "losing_team": '',
    # "loser": '',
    # "results": '',
    # "time": '',
    # "winning_point": '',
    # "losing_point": ''


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
    pass
    # event.number_matches = len(matches)


def record_event_matches(browser, season, division, league, team, event, stats):
    match_list = create_match_list(browser, event)