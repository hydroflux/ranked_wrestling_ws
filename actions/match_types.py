from variables.matches import unknown_values

from actions.summary_breakdown import (handle_blank_participants,
                                       handle_double_disqualification,
                                       handle_double_forfeit, handle_match_bye,
                                       handle_vs_match, split_match_result,
                                       split_runner_up_information,
                                       split_winner_information)


def handle_standard_match(match, summary):
    split_winner_information(match, summary)
    if match.winner not in unknown_values:
        split_runner_up_information(match, summary)
    split_match_result(match)


def handle_match_types(match, summary):
    if ' vs. ' in summary:
        handle_vs_match(match, summary)
    elif summary.endswith('Double Forfeit'):
        handle_double_forfeit(match, summary)
    elif summary.endswith('Double Disqualification'):
        handle_double_disqualification(match, summary)
    elif '[winner] over [loser]' in summary:
        handle_blank_participants(match, summary)
    elif ' over ' in summary:
        handle_standard_match(match, summary)
    elif summary.endswith(' received a bye'):
        handle_match_bye(match, summary)
