class Division:

    number_of_divisions = 0

    def __init__(self, value, type, state, state_abbreviation, name, division_abbreviation,
                 number_leagues=0, leagues=None
    ):
        self.value = value
        self.type = type
        self.state = state
        self.state_abbreviation = state_abbreviation
        self.name = name
        self.division_abbreviation = division_abbreviation
        self.number_leagues = number_leagues
        self.leagues = leagues

        Division.number_of_divisions += 1

    def __str__(self):
        return f'{self.state} {self.type} - {self.name} ({self.division_abbreviation})'
