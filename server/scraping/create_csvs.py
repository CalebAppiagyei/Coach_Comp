import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

years = range(2000, 2024)

for year in years:
    try:
        # Offense
        # Reading the html page as a string
        with open(f"offense/off_pages/{year}.html") as f:
            off_page = f.read()
        
        # Parsing the html string
        off_soup = BeautifulSoup(off_page, "html.parser")
        off_table = off_soup.find(id="team_stats")
        if off_table:
            # Decomposing the unwanted header row and footer
            off_table.find('tfoot').decompose()
            header_row = off_table.find('tr', class_="over_header")
            if header_row:
                header_row.decompose()
                
            # Parsing the table and creating a csv
            offense = pd.read_html(StringIO(str(off_table)))[0]
            offense.to_csv(f"offense/csv/{year}_offense.csv", index=False)
            print(f"Processed offense for {year}")
        else:
            print(f"No offense table found for {year}")
            
        # Defense
        with open(f"defense/def_pages/{year}.html") as f:
            def_page = f.read()
            
        def_soup = BeautifulSoup(def_page, "html.parser")
        def_table = def_soup.find(id="team_stats")
        if def_table:
            def_table.find('tfoot').decompose()
            header_row2 = def_table.find('tr', class_="over_header")
            if header_row2:
                header_row2.decompose()
                
            defense = pd.read_html(StringIO(str(def_table)))[0]
            defense.to_csv(f"defense/csv/{year}_defense.csv", index=False)
            print(f"Processed defense for {year}")
        else:
            print(f"No defense table found for {year}")
    except Exception as e:
        print(f"Error processing year {year}: {e}")