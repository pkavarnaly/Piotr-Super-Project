from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="d:\selenium browser drivers\chromedriver.exe")
        print("Launching Chrome browser..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="d:\selenium browser drivers\geckodriver.exe")
        print("Launching Firefox browser..........")
    else:
        driver = webdriver.Ie(executable_path="C:\Program Files\Internet Explorer\iexplore.exe")
        print("Launching IE browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########### PyTest HTML Report #########

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Piotr Super Project'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Piotr Cavarnali'

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

