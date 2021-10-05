from actions.frame_handling import switch_to_page_frame

from selenium_utilities.locators import locate_element_by_id

from variables.general import main_table_id


def get_page_data(browser):
    switch_to_page_frame(browser)
    return locate_element_by_id(browser, main_table_id, "main page table")
