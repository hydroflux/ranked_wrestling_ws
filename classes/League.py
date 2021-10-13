class League:

    number_of_leagues = 0

    def __init__(self, name, link, number_teams=0, teams=None):
        self.name = name
        self.link = link
        self.number_teams = number_teams
        self.teams = teams

        League.number_of_leagues += 1

    def __str__(self):
        return f'{self.name}: {self.number_teams} teams ({self.link})'