from selenium_utilities.locators import locate_element_by_id
from variables.iframes import (header_frame_id, page_frame_id,
                               page_grid_frame_id, search_frame_id)


def switch_to_page_frame(browser):
    browser.switch_to.default_content()
    page_frame = locate_element_by_id(browser, page_frame_id, "page frame")
    browser.switch_to.frame(page_frame)


def switch_to_page_grid_frame(browser):
    browser.switch_to.default_content()
    page_frame = locate_element_by_id(browser, page_grid_frame_id, "page grid frame")
    browser.switch_to.frame(page_frame)


def switch_to_search_frame(browser):
    browser.switch_to.default_content()
    search_frame = locate_element_by_id(browser, search_frame_id, "search frame")
    browser.switch_to.frame(search_frame)


def switch_to_header_frame(browser):
    browser.switch_to.default_content()
    header_frame = locate_element_by_id(browser, search_frame_id, "header frame")
    browser.switch_to.frame(header_frame)
