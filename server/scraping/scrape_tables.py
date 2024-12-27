import requests
import time
import random
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

years = range(2008, 2024)
off_url = 'https://www.pro-football-reference.com/years/{}/'
def_url = 'https://www.pro-football-reference.com/years/{}/opp.htm'

for year in years:
    o_url = off_url.format(year)
    driver.get(o_url)
    driver.execute_script("window.scrollTo(1, 10000)")
    WebDriverWait(driver, 180).until(
        EC.presence_of_element_located((By.ID, "team_stats"))
    )    
    html = driver.page_source
    with open("offense/off_pages/{}.html".format(year), "w", encoding="utf-8") as f:
            f.write(html)

# for year in years:
#     try:
#         d_url = def_url.format(year)
#         def_data = requests.get(d_url)
#         def_data.raise_for_status() # Raises an exception for HTTP errors
            
#         with open("defense/def_pages/{}.html".format(year), "w") as f:
#             f.write(def_data.text)
            
#         print(f"Successfully downloaded and saved pages for year {year}")
        
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to download pages for year {year}: {e}")
        
#     sleep_time = random.uniform(2, 5)
#     print(f"Sleeping for {sleep_time:.2f} seconds before next iteration...")
#     time.sleep(sleep_time)