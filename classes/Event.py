class Event:

    total_events = 0

    def __init__(self, name, link, date, time, level,
                 type=None, is_tournament=False,
                 number_matches=0, matches=None,
                 #  Dual Event
                 official='', comment='', team_one='',
                 team_one_score='', team_two='', team_two_score='',
                 #  Tournament
                 tournament_winner='', tournament_runner_up=''
        ):
        self.name = name
        self.link = link
        self.date = date
        self.time = time
        self.level = level
        self.type = type
        self.number_matches = number_matches
        self.matches = matches

        # Dual Event
        self.official = official
        self.comment = comment
        self.team_one = team_one
        self.team_one_score = team_one_score
        self.team_two = team_two
        self.team_two_score = team_two_score

        # Tournament
        self.is_tournament = is_tournament
        self.tournament_winner = tournament_winner
        self.tournament_loser = tournament_runner_up

        Event.total_events += 1

    def __str__(self):
        return (f'{self.name} - {self.level} ({self.date} @ {self.time}): \n'
                f'{self.number_matches} matches ({self.link})')
    