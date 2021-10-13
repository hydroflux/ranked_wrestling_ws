from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings.timers import timeout


def print_timeout_statement(type):
    print(f'Browser timed out trying to locate "{type}", please review.')


def locate_element_by_id(locator, id, type, clickable=False, quick=False):
    try:
        if not quick:
            if clickable:
                element_present = EC.element_to_be_clickable((By.ID, id))
            else:
                element_present = EC.presence_of_element_located((By.ID, id))
            WebDriverWait(locator, timeout).until(element_present)
        element = locator.find_element_by_id(id)
        return element
    except TimeoutException:
        print_timeout_statement(type)


def locate_element_by_class_name(locator, class_name, type, clickable=False, quick=False):
    try:
        if not quick:
            if clickable:
                element_present = EC.element_to_be_clickable((By.CLASS_NAME, class_name))
            else:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, class_name))
            WebDriverWait(locator, timeout).until(element_present)
        element = locator.find_element_by_class_name(class_name)
        return element
    except TimeoutException:
        print_timeout_statement(type)
    except NoSuchElementException:
        return False


def locate_elements_by_class_name(locator, class_name, type, clickable=False, quick=False):
    try:
        if not quick:
            if clickable:
                elements_present = EC.element_to_be_clickable((By.CLASS_NAME, class_name))
            else:
                elements_present = EC.presence_of_element_located((By.CLASS_NAME, class_name))
            WebDriverWait(locator, timeout).until(elements_present)
        elements = locator.find_elements_by_class_name(class_name)
        return elements
    except TimeoutException:
        print_timeout_statement(type)


def locate_element_by_name(locator, name, type, clickable=False, quick=False):
    try:
        if not quick:
            if clickable:
                element_present = EC.element_to_be_clickable((By.NAME, name))
            else:
                element_present = EC.presence_of_element_located((By.NAME, name))
            WebDriverWait(locator, timeout).until(element_present)
        element = locator.find_element_by_name(name)
        return element
    except TimeoutException:
        print_timeout_statement(type)


def locate_element_by_tag_name(locator, tag_name, type, clickable=False, quick=False):
    try:
        if not quick:
            if clickable:
                element_present = EC.element_to_be_clickable((By.TAG_NAME, tag_name))
            else:
                element_present = EC.presence_of_element_located((By.TAG_NAME, tag_name))
            WebDriverWait(locator, timeout).until(element_present)
        element = locator.find_element_by_tag_name(tag_name)
        return element
    except TimeoutException:
        print_timeout_statement(type)


def locate_elements_by_tag_name(locator, tag_name, type, clickable=False, quick=False):
    try:
        if not quick:
            if clickable:
                elements_present = EC.element_to_be_clickable((By.TAG_NAME, tag_name))
            else:
                elements_present = EC.presence_of_element_located((By.TAG_NAME, tag_name))
            WebDriverWait(locator, timeout).until(elements_present)
        elements = locator.find_elements_by_tag_name(tag_name)
        return elements
    except TimeoutException:
        print_timeout_statement(type)
