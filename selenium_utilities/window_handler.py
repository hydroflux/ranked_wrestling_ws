from selenium.common.exceptions import WebDriverException


def get_window_handles(browser):
    windows = browser.window_handles
    if len(windows) > 2:
        print(f'Browser located "{str(len(windows))}" tabs, please review.')
        input()
    else:
        return windows


def switch_to_tab(browser, window, type, alt):
    try:
        browser.switch_to.window(browser.window_handles[window])
    except WebDriverException:
        if not alt:
            print(f'Failed to switch to "{type}" window tab, please review.')
            input()


def switch_to_event_tab(browser, alt=False):
    windows = get_window_handles(browser)
    if len(windows) == 2:
        switch_to_tab(browser, 1, "event", alt)
    return windows


def close_event_tab(browser):
    windows = switch_to_event_tab(browser, alt=True)
    if len(windows) == 2:
        browser.close()
    switch_to_tab(browser, 0, "main", alt=False)
    