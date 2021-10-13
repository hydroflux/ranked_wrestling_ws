# BACKLOG

## General To Do

- [ ] Add timers
- [ ] Keep all higher level attributes on the lower level class instances in order to avoid passing as many variables back and forth while recording
- [ ] Consider refactoring 'count_leagues' and 'count_teams' into unified 'count' functions--very similar series of functions ('get_number...', 'report...', 'count...')
- [ ] 'get_league_links' and 'get_team_links' are, as above, almost identical functions
- [ ] 'add_teams' and 'add_leagues' are identical other than a frame switch
- [ ] Create 'build_team_link' and 'build_league_link' functions to match the 'build_event_link' function
- [ ] Create a path for multiple pages of events in the 'events' actions script--currently have a print statement with an input to catch the first multi-page event the application comes across

## Classes & Objects

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
