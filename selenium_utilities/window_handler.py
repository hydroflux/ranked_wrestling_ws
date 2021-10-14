from selenium.common.exceptions import WebDriverException


def get_window_handles(browser):
    windows = browser.window_handles
    if len(windows) != 2:
        print(f'Browser located "{str(windows)}" tabs, please review.')
        input()
    else:
        return windows


def switch_to_tab(browser, window, type):
    try:
        browser.switch_to.window(browser.window_handles[window])
    except WebDriverException:
        print(f'Failed to switch to "{type}" window tab, please review.')
        input()


def switch_to_event_tab(browser):
    windows = get_window_handles(browser)
    switch_to_tab(browser, windows[1], "event")
    return windows


def close_event_tab(browser):
    windows = switch_to_event_tab(browser)
    browser.close()
    switch_to_tab(browser, windows[0], "main")
    