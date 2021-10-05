from actions.frame_handling import switch_to_page_frame
from actions.pages import get_page_handler


def get_number_leagues(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


def report_number_leagues(division):
    print(f'Total Leagues for the {division.name} Division:\n'
          f'{division.number_leagues}')


def count_leagues(browser, division):
    page_handler = get_page_handler(browser)
    division.number_leagues += get_number_leagues(page_handler)
    report_number_leagues(division)


def create_league_list(browser, season, division):
    count_leagues(browser, division)
