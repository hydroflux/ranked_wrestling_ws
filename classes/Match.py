class Match:

    total_matches = 0

    def __init__(self, weight, summary, stat_flag, tw_event
    ):
        self.weight = weight
        self.summary = summary
        self.stat_flag = stat_flag
        self.tw_event = tw_event

        Match.total_matches += 1


    def __str__(self):
        return (f'{self.summary} ({self.weight})')