class Tournament:

    total_tournaments = 0

    def __init__(self, name='', link='', official='', team_one='', team_two='',
                 team_one_score='', team_two_score='', comment='',
                 number_events=0, events=None
        ):
        self.name = name
        self.link = link
        self.official = official
        self.team_one = team_one
        self.team_two = team_two
        self.team_one_score = team_one_score
        self.team_two_score = team_two_score
        self.comment = comment
        self.number_events = number_events
        self.events = events

        Tournament.total_tournaments += 1

    def __str__(self):
        return (f'{self.name}: \n'
                f'{self.number_events} events ({self.link})')
