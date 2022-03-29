import os

import pytest
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

from Config.config import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Pass the browser name"
    )


@pytest.fixture(scope="class")
def setup(request):
    try:
        browser_name = request.config.getoption("browser_name")
    except:
        browser_name = TestData.BROWSER_NAME

    if browser_name == "chrome":
        driverPath = os.path.realpath("chromedriver.exe")
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.add_argument("--start-maximized")
        if "Tests" not in driverPath:
            driverPath = os.path.join('Drivers', 'chromedriver.exe')
        else:
            driverPath = driverPath.replace('Tests', 'Drivers')
        driver = webdriver.Chrome(executable_path=driverPath, options=ChromeOptions)

    elif browser_name == "edge":
        driverPath = os.path.realpath("msedgedriver.exe")
        options = EdgeOptions()
        options.use_chromium = True
        if "Tests" not in driverPath:
            driverPath = os.path.join('Drivers', 'msedgedriver.exe')
        else:
            driverPath = driverPath.replace('Tests', 'Drivers')
        driver = Edge(executable_path=driverPath, options=options)

    driver.get(TestData.BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
