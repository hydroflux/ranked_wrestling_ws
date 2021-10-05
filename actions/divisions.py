from selenium.webdriver.support.ui import Select
from actions.frame_handling import switch_to_page_frame
from actions.main_menu import select_menu_option
from selenium_utilities.inputs import click_button
from selenium_utilities.locators import locate_element_by_id
from selenium_utilities.open import assert_window_title
from settings.general_functions import script_execution

from variables.general import division_menu_id, alt_division_menu_id, search_button_id
from variables.scripts import division_script, alt_division_script


def select_division(browser, division, alt):
    menu_id = division_menu_id if alt else alt_division_menu_id
    selector = Select(browser.find_element_by_id(menu_id))
    selector.select_by_value(division.value)


def open_division(browser, alt):
    script = alt_division_script if alt else division_script
    script_execution(browser, script)


def open_division(browser, season, division, alt=False):
    select_division(browser, division, alt)
    open_division(browser, alt)
    assert_window_title(browser, season.title)
    return division


def open_division_leagues(browser, season, division):
    select_menu_option(browser)
    switch_to_page_frame(browser)
    click_button(browser, locate_element_by_id, search_button_id, "search button")
    open_division(browser, season, division, alt=True)