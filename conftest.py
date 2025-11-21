import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            service = FirefoxService()
            return webdriver.Firefox(service=service, options=options)
        elif browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            service = ChromeService()
            return webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", 
        help="Выбор браузера: 'chrome' или 'firefox'."
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    yield driver
    driver.quit()