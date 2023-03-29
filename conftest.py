import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from fake_useragent import UserAgent
ua = UserAgent
ua.chrome
@pytest.fixture()
def driver():
    #driver_service = Service()
    #options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    #options.add_argument(useragent)
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    #options.add_argument("--headless")
    #driver = webdriver.Chrome(service=driver_service, options=options)
    #driver.maximize_window()
    #driver.delete_all_cookies()
    yield driver
    #driver.quit()
