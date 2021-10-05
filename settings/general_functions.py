from itertools import groupby

from settings.timers import short_nap


def script_execution(browser, script):
    browser.execute_script(script)
    short_nap()


def get_list_element_text(list):
    return [item.text for item in list]


def all_equal(iterable):
    group = groupby(iterable)
    return next(group, True) and not next(group, False)


def get_direct_link(link_element):
    return link_element.get_attribute("href")
