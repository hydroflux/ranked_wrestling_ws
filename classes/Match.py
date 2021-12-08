class Match:

    total_matches = 0

    def __init__(self, weight, summary, level='', round='',
                 winning_team='', winner='', losing_team='', loser='',
                 result='', time='', point=None, winning_point='', losing_point='',
                 stat_flag='', tw_event='',
                 official='', comment='', team_one='', team_one_score='', team_two='', team_two_score=''

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
        self.official = official
        self.comment = comment
        self.team_one = team_one
        self.team_one_score = team_one_score
        self.team_two = team_two
        self.team_two_score = team_two_score

        Match.total_matches += 1


    def __str__(self):
        return (f'{self.summary} ({self.weight})')
