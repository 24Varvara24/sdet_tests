import pytest
from selenium import webdriver

from selenium.webdriver.edge.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')
    _driver = webdriver.Edge(options=options)
    _driver.get('http://uitestingplayground.com/')
    yield _driver
    _driver.quit()
