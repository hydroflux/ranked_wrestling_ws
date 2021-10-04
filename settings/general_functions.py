from settings.timers import short_nap

def script_execution(browser, script):
    browser.execute_script(script)
    short_nap()