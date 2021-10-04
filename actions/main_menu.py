from variables.general import main_menu_id, main_menu_options_tag
from selenium_utilities.locators import locate_element_by_id, locate_elements_by_tag_name


def get_menu(browser):
    browser.switch_to.default_content()
    return locate_element_by_id(browser, main_menu_id, "menu")


def get_menu_options(browser):
    menu = get_menu(browser)
    return locate_elements_by_tag_name(menu, main_menu_options_tag, "menu options", True)


def select_menu_option(browser, option=None):
    menu_options = get_menu_options(browser)
    if option is None:
        menu_options[2].click()
