import requests
import time
import random

years = range(2000, 2024)
off_url = 'https://www.pro-football-reference.com/years/{}/'
def_url = 'https://www.pro-football-reference.com/years/{}/opp.htm'

for year in years:
    try:
        o_url = off_url.format(year)
        off_data = requests.get(o_url)
        off_data.raise_for_status()  # Raises an exception for HTTP errors
        
        d_url = def_url.format(year)
        def_data = requests.get(d_url)
        def_data.raise_for_status()
        
        with open("offense/off_pages/{}.html".format(year), "w") as f:
            f.write(off_data.text)
            
        with open("defense/def_pages/{}.html".format(year), "w") as f:
            f.write(def_data.text)
            
        print(f"Successfully downloaded and saved pages for year {year}")
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to download pages for year {year}: {e}")
        
    sleep_time = random.uniform(2, 5)
    print(f"Sleeping for {sleep_time:.2f} seconds before next iteration...")
    time.sleep(sleep_time)