def center_element(browser, element):
    desired_y = (element.size['height'] / 2) + element.location['y']
    window_h = browser.execute_script('return window.innerHeight')
    window_y = browser.execute_script('return window.pageYOffset')
    current_y = (window_h / 2) + window_y
    scroll_y_by = desired_y - current_y
    browser.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)


def click_button(browser, locator_function, attribute, type):
    button = locator_function(browser, attribute, type, True)
    center_element(browser, button)
    button.click()
