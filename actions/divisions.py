from selenium.webdriver.support.ui import Select
from settings.general_functions import script_execution

from variables.general import division_menu_id
from variables.divisions import divisions
from variables.scripts import division_script


def select_division(browser, division):
    selector = Select(browser.find_element_by_id(division_menu_id))
    selector.select_by_value(division.value)


def open_division(browser, state):
    division = divisions[state]
    select_division(browser, division)
    script_execution(browser, division_script)
    return division
