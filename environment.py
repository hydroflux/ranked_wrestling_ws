from settings.driver import create_webdriver

def execute(headless):
    browser = create_webdriver(False)
