class Stats:

    number_stats = 0

    def __init__(self, league, city, tournament, match):
        self.league = league
        self.city = city
        self.tournament = tournament
        self.match = match

        Stats.number_stats += 1

    def __str__(self):
        return f'{self.league} - {self.city} => {self.match}'
