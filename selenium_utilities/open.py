def assert_window_title(browser, page_title):
    print('page_title', page_title)
    try:
        assert page_title in browser.title.strip()
        return True
    except AssertionError:
        return False


def print_failed_window_assertion_statement(page_type):
    print(f'Browser failed to successfully open "{page_type}", please review.')
    input()


def handle_failed_window_assertion(browser, page_type):
    print_failed_window_assertion_statement(page_type)
    if page_type == 'open site':
        browser.close()
        quit()


def open_url(browser, url, page_title, page_type):
    browser.get(url)
    if not assert_window_title(browser, page_title):
        handle_failed_window_assertion(browser, page_type)
