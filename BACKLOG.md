# BACKLOG

## General To Do

- [ ] Add timers
- [ ] Keep all higher level attributes on the lower level class instances in order to avoid passing as many variables back and forth while recording
- [ ] Fix 'NoSuchElementException', 'NoSuchWindowException', and 'StaleElementException' appearing during some login processes
- [ ] Figure out why Flake8 isn't working properly (check abstractor for settings?)
- [ ] Add print statements for '# out of #' for each level of abstraction
- [ ] Create a way to handle whether an event is a tournament or not in 'Matches' & the 'Stat' class

## Actions

### Leagues

- [ ] Consider refactoring 'count_leagues' and 'count_teams' into unified 'count' functions--very similar series of functions ('get_number...', 'report...', 'count...')
- [ ] 'get_league_links' and 'get_team_links' are, as above, almost identical functions
- [ ] 'add_teams' and 'add_leagues' are identical other than a frame switch
- [ ] Create a 'build_league_link' function similar to the 'build_event_link' function in 'events' script

### Teams

- [ ] Create a 'build_team_link' function similar to the 'build_event_link' function in 'events' script

### Events

- [ ] Need to add functions to check columns & column headers before deciding on where attribute data comes from
- [ ] Add window handling for opening & closing events
- [ ] Update 'Event' class after looking through additional event attributes
- [ ] Create a path for multiple pages of events in the 'events' actions script--currently have a print statement with an input to catch the first multi-page event the application comes across
- [ ] Figure out some way to do a 'total event' count to compare against the event list
- [ ] Create a 'validate_event_list' function after completing the above

### Matches

- [ ] Create a method to check the match headers before creating a 'Match' object

## Classes & Objects

- [ ] Create nested classes
- [ ] Do a gap analysis of the "Stats" class vs. the 'stats' object to determine the best way to proceed
- [ ] Benefits of using "Stats" class: Hold ids, class_names, and tag_names in the class instance

## Invalid Searches

- [ ] Update the 'record_invalid_league' function
- [ ] Update the 'record_invalid_team' function

## Interface

- [ ] Create a way to prompt the user for 'season', 'headless', and 'state', etc.

## Selenium Utilities

### Locators

- [ ] Implement a 'quick' option to skip the WebDriverWait to locator functions
