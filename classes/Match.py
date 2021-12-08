class Match:

    total_matches = 0

    def __init__(self, weight, summary, stat_flag, tw_event, level='',
                 round='', winning_team='', winner='',
                 losing_team='', loser='', result='', time='',
                 point=None, winning_point='', losing_point=''
    ):
        self.weight = weight
        self.summary = summary
        self.stat_flag = stat_flag
        self.tw_event = tw_event
        self.level = level
        self.round = round
        self.winning_team = winning_team
        self.winner = winner
        self.losing_team = losing_team
        self.loser = loser
        self.result = result
        self.time = time
        self.point = point
        self.winning_point = winning_point
        self.losing_point = losing_point

        Match.total_matches += 1


    def __str__(self):
        return (f'{self.summary} ({self.weight})')
