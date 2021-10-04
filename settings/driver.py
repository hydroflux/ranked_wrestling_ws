from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def chrome_webdriver(headless):
    chromedriver = ChromeDriverManager().install()
    options = webdriver.ChromeOptions()

    if headless: options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # Bypass OS Security Model
    options.add_argument("--disable-infobars")  # https://stackoverflow.com/a/43840128/1689770
    options.add_argument("--disable-browser-side-navigation")  # https://stackoverflow.com/a/49123152/1689770
    options.add_argument('enable-automation')  # https://stackoverflow.com/a/43840128/1689770

    driver = webdriver.Chrome(chromedriver, options=options)
    driver.maximize_window()
    return driver


def create_webdriver(headless):
    browser = chrome_webdriver(headless)
    return browser
