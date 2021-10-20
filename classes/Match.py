class Match:

    total_matches = 0

    def __init__(self, weight, summary, stat_flag, tw_event,
                 tournament_info=None
    ):
        self.weight = weight
        self.summary = summary
        self.stat_flag = stat_flag
        self.tw_event = tw_event
        self.tournament_info = tournament_info

        Match.total_matches += 1


    def __str__(self):
        return (f'{self.summary} ({self.weight})')
