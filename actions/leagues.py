from actions.frame_handling import switch_to_page_frame
from actions.pages import get_page_handler


def get_number_leagues(page_handler):
    handler_text = page_handler.text
    return int(handler_text[handler_text.rfind(' ') + 1:])


def count_leagues(browser, division):
    page_handler = get_page_handler(browser)
    division.number_leagues += get_number_leagues(page_handler)


def create_league_list(browser, season, division):
    pass
