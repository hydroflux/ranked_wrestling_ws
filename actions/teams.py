from actions.pages import get_page_data, get_page_handler


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


def get_team_links(page_data):
    team_links = []


def add_page_teams(browser, league, team_list):
    page_data = get_page_data(browser, False)
    team_links = get_team_links(page_data)
    team_list.extend(team_links)
    print(f'Added {str(len(team_links))} teams to "{league.name}" team list.')


def add_teams(browser, league, team_list):
    add_page_teams(browser, league, team_list)


def validate_team_list():
    pass


def create_team_list(browser, league):
    team_list = []
    team_list = add_teams(browser, league, team_list)


def update_league_teams():
    pass


def report_teams():
    pass


def check_for_team_results():
    pass


def search_team():
    pass


def record_teams():
    pass


def record_league_teams(browser, season, division, league, stats):
    count_teams(browser, league)
    team_list = create_team_list(browser, league)
