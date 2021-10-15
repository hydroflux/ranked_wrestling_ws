class Tournament:

    total_tournaments = 0

    def __init__(self, name, link, number_events=0, events=None):
        self.name = name
        self.link = link
        self.number_events = number_events
        self.events = events

        Tournament.total_tournaments += 1

    def __str__(self):
        return (f'{self.name}: \n'
                f'{self.number_events} events ({self.link})')
