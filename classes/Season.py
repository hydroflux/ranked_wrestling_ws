from variables.scripts import season_script

class Season:
    def __init__(self, id, name, type, year, title):
        self.id = id
        self.name = name
        self.type = type
        self.year = year
        self.title = title

    def __str__(self):
        return f'{self.name} {self.year} ({self.id})'

    def season_link(self):
        return f'{season_script}("{self.id}")'