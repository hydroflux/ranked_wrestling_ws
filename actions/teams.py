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


def record_teams(browser, season, division, league, stats):
    count_teams(browser, league)