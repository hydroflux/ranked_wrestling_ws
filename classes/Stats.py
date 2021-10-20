class Stat:

    number_stats = 0

    def __init__(
        self,
        state, division_name, division_abbreviation, number_leagues,
        league_name, league_link, number_teams,
        team_name, team_link, team_abbreviation, number_events,
        event_name, date, time, level, type, number_matches,
        weight, summary, stat_flag, tw_event, match_level, round,
        winning_team, winner, losing_team, loser,
        results, match_time, winning_point, losing_point
    ):
        self.state = state
        self.division_name = division_name
        self.division_abbreviation = division_abbreviation
        self.number_leagues = number_leagues
        self.league_name = league_name
        self.league_link = league_link
        self.number_teams = number_teams
        self.team_name = team_name
        self.team_link = team_link
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
        self.stat_flag = stat_flag
        self.tw_event = tw_event
        self.match_level = match_level
        self.round = round
        self.winning_team = winning_team
        self.winner = winner
        self.losing_team = losing_team
        self.loser = loser
        self.results = results
        self.match_time = match_time
        self.winning_point = winning_point
        self.losing_point = losing_point

        Stat.number_stats += 1

    def __str__(self):
        return f'{self.league} - {self.city} => {self.match}'
