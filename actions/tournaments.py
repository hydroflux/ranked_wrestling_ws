def update_event_and_tournament_name(event):
    event.tournament_name = event.name
    event.name = ''
    pass


# 'tournaments' have the same general structure as 'events'
def record_tournament(browser, division, league, team, event, stats):
    update_event_and_tournament_name(event)
    print('Press enter to continue...')
    input()