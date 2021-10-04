class Division:

    number_of_divisions = 0

    def __init__(self, value, type, state, state_abbreviation, name, division_abbreviation):
        self.value = value
        self.type = type
        self.state = state
        self.state_abbreviation = state_abbreviation
        self.name = name
        self.division_abbreviation = division_abbreviation

        Division.number_of_divisions += 1

    def __str__(self):
        return f'{self.state} {self.type} - {self.name} ({self.abbreviation})'
