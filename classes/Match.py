class Match:

    total_matches = 0

    def __init__(self, weight, summary, level='', round='',
                 winning_team='', winner='', losing_team='', loser='',
                 result='', time='', point=None, winning_point='', losing_point='',
                 stat_flag='', tw_event='',
                 team_one_point='', team_two_point=''

    ):
        self.weight = weight
        self.summary = summary
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

        # Single Match
        self.stat_flag = stat_flag
        self.tw_event = tw_event

        # Dual Match
        self.team_one_point = team_one_point
        self.team_two_point = team_two_point

        Match.total_matches += 1


    def __str__(self):
        return (f'{self.summary} ({self.weight})')
