from selenium.webdriver.support.ui import Select
from actions.frame_handling import switch_to_page_frame
from selenium_utilities.inputs import click_button
from selenium_utilities.locators import locate_element_by_id
from selenium_utilities.open import assert_window_title
from settings.general_functions import script_execution

from variables.general import division_menu_id, alt_division_menu_id, search_button_id
from variables.divisions import divisions
from variables.scripts import division_script, alt_division_script


def select_division(browser, division, alt):
    if alt: division_menu_id = alt_division_menu_id
    selector = Select(browser.find_element_by_id(division_menu_id))
    selector.select_by_value(division.value)


def open_division(browser, alt):
    if alt: division_script = alt_division_script
    script_execution(browser, division_script)


def open_division(browser, season, state, alt=False):
    division = divisions[state]
    select_division(browser, division, alt)
    open_division(browser, alt)
    assert_window_title(browser, season.title)
    return division


def open_division_leagues(browser, season):
    switch_to_page_frame(browser)
    click_button(browser, locate_element_by_id, search_button_id, "search button")
    open_division(browser, season, alt=True)