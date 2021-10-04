from selenium_utilities.locators import locate_element_by_id
from variables.iframes import (header_frame_id, page_frame_id,
                               page_grid_frame_id, search_frame_id)


def switch_to_frame(browser, id, type):
    browser.switch_to.default_content()
    frame = locate_element_by_id(browser, id, type)
    browser.switch_to.frame(frame)


def switch_to_page_frame(browser):
    switch_to_frame(browser, page_frame_id, "page frame")


def switch_to_page_grid_frame(browser):
    switch_to_frame(browser, page_grid_frame_id, "page grid frame")


def switch_to_search_frame(browser):
    switch_to_frame(browser, search_frame_id, "search frame")


def switch_to_header_frame(browser):
    switch_to_frame(browser, search_frame_id, "header frame")
