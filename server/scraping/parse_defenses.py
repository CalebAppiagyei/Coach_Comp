import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *

load_dotenv()

db_url = os.getenv("DB_URL")
engine = create_engine(db_url, echo=True)
Base = declarative_base()

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()

years = range(2000, 2024)
for year in years:
    # Reading the defensive data
    teams = pd.read_csv(f"defense/csv/{year}_defense.csv")
    for index, row in teams.iterrows():
        # Entering the defensive stats for each team
        team = session.query(Team).filter(Team.team_name == row['Tm'], Team.year == year).one()
        
        tot_def = TotalDefensiveData(
            team_id=team.team_id,
            pa=row['PA'],
            yds=row['Yds'], 
            plays=row['Ply'], 
            ypp=row['Y/P'], 
            turnovers=row['TO'], 
            penalties=row['Pen'], 
            pen_yds=row['Yds.3'], 
            firstd=row['1stD']) 
        
        p_def = PassingDefensiveData(
            team_id=team.team_id,
            completions=row['Cmp'],
            attempts=row['Att'],
            yards=row['Yds.1'],
            touchdowns=row['TD'],
            interceptions=row['Int'],
            nya=row['NY/A'],
            first_downs=row['1stD.1']
        )
        
        r_def = RushingDefensiveData(
            team_id=team.team_id,
            attempts=row['Att.1'],
            yards=row['Yds.2'],
            touchdowns=row['TD.1'],
            ypa=row['Y/A'],
            first_downs=row['1stD.2']
        )
        
        session.add_all([tot_def, p_def, r_def])
        
session.commit()
session.close()
