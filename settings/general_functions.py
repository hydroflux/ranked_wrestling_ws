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


def iterate_list(list, web_element=None):
    if web_element is None:
        return [(f'{element}') for element in list]
    else:
        return [(f'{element.text}') for element in list]


def print_list_by_index(list, web_element=None):
    if web_element is None:
        [print(list.index(element), element, '\n-------------------------') for element in list]
    else:
        [print(list.index(element), element.text, '\n-------------------------') for element in list]