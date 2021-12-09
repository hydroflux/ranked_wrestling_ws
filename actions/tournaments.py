def update_event_and_tournament_name(event):
    event.tournament_name = event.name
    event.name = ''


def build_event_link(browser, tournament_event_information):
    pass


def get_tournament_event_links(browser):
    pass


def add_page_tournament_events(browser, team, event, tournament_event_list):
    pass


def add_tournament_events(browser, team, event, tournament_event_list):
    add_page_tournament_events(browser, team, event, tournament_event_list)
    while len(tournament_event_list) < event.number_tournament_events:
        print('Encountered multiple tournament event pages, please review, update code, & re-start.')
        input('Press enter to continue...')
    return tournament_event_list


# validate_tournament_events


def create_tournament_event_list(browser, team, event):
    tournament_event_list = []
    return add_tournament_events(browser, team, event, tournament_event_list)


def update_tournament_events(team, event, tournament_event_list):
    pass


def report_tournament_events(league, team, event):
    pass


def open_tournament_event(browser, event):
    pass


def search_tournament_event(browser ,division, league, team, event, stats):
    pass


def record_tournament_events(browser, division, league, team, event, stats):
    pass


# 'tournaments' have the same general structure as 'events'
def record_tournament(browser, division, league, team, event, stats):
    update_event_and_tournament_name(event)
    tournament_event_list = create_tournament_event_list(browser, team, event)
    # update_tournament_events(team, event, tournament_event_list)
    # report_tournament_events(league, team, event)
    print('Press enter to continue...')
    input()