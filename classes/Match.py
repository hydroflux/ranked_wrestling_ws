class Match:

    total_matches = 0

    def __init__(self, weight, summary, stat_flag, tw_event, level=None,
                 rounds=None, winning_team=None, winner=None,
                 losing_team=None, loser=None, results=None,
                 time=None, winning_point=None, losing_point=None
    ):
        self.weight = weight
        self.summary = summary
        self.stat_flag = stat_flag
        self.tw_event = tw_event
        self.level = level
        self.rounds = rounds
        self.winning_team = winning_team
        self.winner = winner,
        self.losing_team = losing_team,
        self.loser = loser,
        self.results = results,
        self.time = time,
        self.winning_point = winning_point,
        self.losing_point = losing_point

        Match.total_matches += 1


    def __str__(self):
        return (f'{self.summary} ({self.weight})')
