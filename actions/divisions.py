from selenium.webdriver.support.ui import Select

from selenium_utilities.inputs import click_button
from selenium_utilities.locators import (locate_element_by_id,
                                         locate_elements_by_class_name)
from selenium_utilities.open import assert_window_title

from settings.general_functions import all_equal, get_list_element_text, script_execution

from variables.general import (alt_division_menu_id, division_menu_id,
                               main_table_divisions_class_name,
                               search_button_id)
from variables.scripts import alt_division_script, division_script

from actions.frame_handling import switch_to_page_frame
from actions.main_menu import select_menu_option
from actions.pages import get_page_data


def select_division(browser, division, alt):
    menu_id = alt_division_menu_id if alt else division_menu_id
    selector = Select(browser.find_element_by_id(menu_id))
    selector.select_by_value(division.value)


def execute_division_option(browser, alt):
    script = alt_division_script if alt else division_script
    script_execution(browser, script)


def open_division(browser, season, division, alt=False):
    select_division(browser, division, alt)
    execute_division_option(browser, alt)
    assert_window_title(browser, season.title)


def check_league_divisions(browser):
    page_data = get_page_data(browser)
    division_elements = locate_elements_by_class_name(page_data, main_table_divisions_class_name, "league divisions")
    division_results = get_list_element_text(division_elements)
    all_equal(division_results)


def validate_league_divisions(browser):
    while not check_league_divisions(browser):
        print('Page not loaded correctly, checking again.')
        check_league_divisions(browser)


def open_division_leagues(browser, season, division):
    select_menu_option(browser)
    switch_to_page_frame(browser)
    click_button(browser, locate_element_by_id, search_button_id, "search button")
    open_division(browser, season, division, alt=True)
