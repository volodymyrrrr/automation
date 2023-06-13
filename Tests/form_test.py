encoding="utf-8"
import csv
import os
import time
import gspread
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from fake_useragent import UserAgent


client = gspread.service_account('Tests/gs_credentials.json')
working_sheet = client.open_by_url(
    'https://docs.google.com/spreadsheets/d/1fRi9qAdb-E-xAY_jQiMdjjEsN1xZZdxK6865V-Ck6RE/edit#gid=0')
wb1 = working_sheet.get_worksheet(0)
URLS = wb1.get_values('B2:G500')
if os.path.exists("links.csv"):
    os.remove("links.csv")
else:
    print("The file does not exist")

with open("links.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(("links", "tangiblee", "number", "popup", "Skip", "useragent"))
for urls in URLS:
    with open("links.csv", 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            urls
        )


def test_cicle(driver):
    with open("links.csv", "r", newline='') as file1:
        reader = csv.DictReader(file1, delimiter=";")
        for line in reader:
            cta = line["tangiblee"]
            url = line["links"]
            r = line["number"]
            popup = line["popup"]
            skip = line["Skip"]
            useragent = line["useragent"]
            if skip == 'TRUE':
                print('scip')
            else:
                driver_service = Service()
                options = webdriver.ChromeOptions()
                options.add_argument("--incognito")
                options.add_argument(useragent)
                # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
                options.add_argument("--headless")
                driver = webdriver.Chrome(service=driver_service, options=options)
                driver.maximize_window()
                driver.delete_all_cookies()
                driver.get(url)
                time.sleep(15)
                try:
                    driver.find_element(By.XPATH, popup).click()
                    driver.execute_script("scrollBy(0,550);")
                    try:
                        Wait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, cta)))
                        wb1.update_cell(row=r, col=8, value="Pass")
                    except:
                        wb1.update_cell(row=r, col=8, value="false")
                except:
                    wb1.update_cell(row=r, col=8, value="Popup_error")
    driver.close()

