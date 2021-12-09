class Stat:

    number_stats = 0

    def __init__(
        self,
        state, division_name, division_abbreviation, number_leagues,
        league_name, number_teams,
        team_name, team_abbreviation, number_events,
        event_name, date, time, level, type, number_matches,
        weight, summary,
        # Single Match Exclusive
        stat_flag, tw_event,
        # Tournament
        is_tournament, tournament_name,
        tournament_winner, tournament_runner_up,
        # Dual Event Exclusive
        official, comment, team_one, team_two,
        team_one_score, team_two_score,
        # Dual Match Exclusive
        team_one_point, team_two_point,
        # Match Summary Breakdown
        match_level, round,
        winning_team, winner, losing_team, loser,
        result, match_time, winning_point, losing_point,
        # Other
        league_link='', team_link=''
    ):
        self.state = state
        self.division_name = division_name
        self.division_abbreviation = division_abbreviation
        self.number_leagues = number_leagues
        self.league_name = league_name
        self.number_teams = number_teams
        self.team_name = team_name
        self.team_abbreviation = team_abbreviation
        self.number_events = number_events
        self.event_name = event_name
        self.date = date
        self.time = time
        self.level = level
        self.type = type
        self.number_matches = number_matches
        self.weight = weight
        self.summary = summary
        # Single Match Exclusive
        self.stat_flag = stat_flag
        self.tw_event = tw_event
        # Tournament
        self.is_tournament = is_tournament
        self.tournament_name = tournament_name
        self.tournament_winner = tournament_winner
        self.tournament_runner_up = tournament_runner_up
        # Dual Event Exclusive
        self.official = official
        self.comment = comment
        self.team_one = team_one
        self.team_one_score = team_one_score
        self.team_two = team_two
        self.team_two_score = team_two_score
        # Dual Match Exclusive
        self.team_one_point= team_one_point
        self.team_two_point= team_two_point
        # Match Summary Breakdown
        self.match_level = match_level
        self.round = round
        self.winning_team = winning_team
        self.winner = winner
        self.losing_team = losing_team
        self.loser = loser
        self.result = result
        self.match_time = match_time
        self.winning_point = winning_point
        self.losing_point = losing_point
        # Other
        self.league_link = league_link
        self.team_link = team_link

        Stat.number_stats += 1

    def __str__(self):
        return f'{self.league_name} - {self.team_name} => {self.summary}'
