from variables.scripts import season_script

class Season:
    def __init__(self, id, type, year):
        self.id = id
        self.type = type
        self.year = year

    def season_link(self):
        return f'{season_script}("{self.id}")'