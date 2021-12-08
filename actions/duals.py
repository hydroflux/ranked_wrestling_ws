
def get_event_dual_information():
    pass


def add_page_dual_matches(browser, event, match_list):
    pass


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
    # General Variables
    official = ''
    comment = ''
    # Team One Variables
    team_one = ''
    team_one_score = ''
    # Team Two Variables
    team_two = ''
    team_two_score = ''
    # match_list = create_dual_match_list(browser, event)
