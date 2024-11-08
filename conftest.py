from selenium import webdriver
import pytest
import helpers


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Can't create instance for this param")
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def user():
    user = helpers.register_new_user_and_return_user_data()
    yield user
    helpers.delete_user(user['json']['accessToken'])
