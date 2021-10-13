class Team:

    total_teams = 0

    def __init__(self, name, link, number_events=0, events=None):
        self.name = name
        self.link = link
        self.number_events = number_events
        self.events = events

        Team.total_teams += 1

    def __str__(self):
        return f'{self.name}: {self.number_events} events ({self.link})'