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
    # Reading the Offensive stats for the year
    teams = pd.read_csv(f"offense/csv/{year}_offense.csv")
    season = session.query(Season).filter(Season.year == year).one()
    for index, row in teams.iterrows():
        # Creating a new team entry
        new_team = Team(team_name=row['Tm'], year=year, games=season.games_played)
        session.add(new_team)
        session.commit()
        
        # Grabbing the new team
        team = session.query(Team).filter(Team.team_name == row['Tm'], Team.year == year, Team.games == season.games_played).one()
        if team:
            # New offensive data entries
            tot_off = TotalOffensiveData(
                team_id=team.team_id, 
                pts_for=row['PF'], 
                yds=row['Yds'], 
                plays=row['Ply'], 
                ypp=row['Y/P'], 
                turnovers=row['TO'], 
                penalties=row['Pen'], 
                pen_yds=row['Yds.3'], 
                firstd=row['1stD'])
            
            p_off = PassingOffensiveData(
                team_id=team.team_id,
                completions=row['Cmp'],
                attempts=row['Att'],
                yards=row['Yds.1'],
                touchdowns=row['TD'],
                interceptions=row['Int'],
                nya=row['NY/A'],
                first_downs=row['1stD.1']
            )
            
            r_off = RushingOffensiveData(
                team_id=team.team_id,
                attempts=row['Att.1'],
                yards=row['Yds.2'],
                touchdowns=row['TD.1'],
                ypa=row['Y/A'],
                first_downs=row['1stD.2']
            )

            session.add_all([tot_off, p_off, r_off])

session.commit()
session.close()