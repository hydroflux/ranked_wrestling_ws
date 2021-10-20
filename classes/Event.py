class Event:

    total_events = 0

    def __init__(self, name, link, date, time, level,
                 type=None, is_tournament=False,
                 number_matches=0, matches=None
        ):
        self.name = name
        self.link = link
        self.date = date
        self.time = time
        self.level = level
        self.type = type
        self.is_tournament = is_tournament
        self.number_matches = number_matches
        self.matches = matches

        Event.total_events += 1

    def __str__(self):
        return (f'{self.name} - {self.level} ({self.date} @ {self.time}): \n'
                f'{self.number_matches} matches ({self.link})')
    