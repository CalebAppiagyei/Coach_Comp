import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *

load_dotenv()
coach_path = os.getenv("COACH_PATH")
db_url = os.getenv("DB_URL")
engine = create_engine(db_url, echo=True)
Base = declarative_base()
    
# Creating the session
Session = sessionmaker(bind=engine)
session = Session()

# Mapping NFL abbreviations to teams
nfl_teams = {
    'ARI': 'Arizona Cardinals',
    'ATL': 'Atlanta Falcons',
    'BAL': 'Baltimore Ravens',
    'BUF': 'Buffalo Bills',
    'CAR': 'Carolina Panthers',
    'CHI': 'Chicago Bears',
    'CIN': 'Cincinnati Bengals',
    'CLE': 'Cleveland Browns',
    'DAL': 'Dallas Cowboys',
    'DEN': 'Denver Broncos',
    'DET': 'Detroit Lions',
    'GNB': 'Green Bay Packers',
    'HOU': 'Houston Texans',
    'IND': 'Indianapolis Colts',
    'JAX': 'Jacksonville Jaguars',
    'KAN': 'Kansas City Chiefs',
    'LVR': 'Las Vegas Raiders',
    'OAK': 'Oakland Raiders',
    'LAC': 'Los Angeles Chargers',
    'SDG': 'San Diego Chargers',
    'LAR': 'Los Angeles Rams',
    'STL': 'St. Louis Rams',
    'MIA': 'Miami Dolphins',
    'MIN': 'Minnesota Vikings',
    'NWE': 'New England Patriots',
    'NOR': 'New Orleans Saints',
    'NYG': 'New York Giants',
    'NYJ': 'New York Jets',
    'PHI': 'Philadelphia Eagles',
    'PIT': 'Pittsburgh Steelers',
    'SFO': 'San Francisco 49ers',
    'SEA': 'Seattle Seahawks',
    'TAM': 'Tampa Bay Buccaneers',
    'TEN': 'Tennessee Titans',
    'WAS': ['Washington Commanders', 'Washington Football Team', 'Washington Redskins']
}

years = range(2000, 2024)
for year in years:
    # Formatting the coach table
    coaches = pd.read_csv(coach_path + "/{}.csv".format(year), header=1)
    coaches = coaches[["Coach", "Tm","G.2", "W.2", "L.2", "T.2", "Remark"]]
    coaches['wl_pct'] = (coaches['W.2'] + (coaches['T.2'] * 0.5)) / coaches['G.2']

    for index, row in coaches.iterrows():
        # Querying each coach
        coach = session.query(CoachData).filter(CoachData.name == row['Coach'], CoachData.games == row['G.2'], CoachData.wl_pct == row['wl_pct']).one()
        team_names = nfl_teams.get(row['Tm'])

        # If there are multiple names associated with the abbreviation (like 'WAS')
        if isinstance(team_names, list):
            team = session.query(Team).filter(Team.team_name.in_(team_names), Team.year == year).one()
        else:
            # If there's only one name associated with the abbreviation
            team = session.query(Team).filter(Team.team_name == team_names, Team.year == year).one()
        
        if team.coach_id == coach.coach_id:
            # If the coach has already been assigned (allows for multiple runs)
            continue
        elif team.coach_id != 1:
            # If the coach has been assigned already but that team had a second coach
            team.extra_info = {"coach" : row['Coach'],
                               "remark" : row['Remark'] if pd.notna(row['Remark']) else ""
                            }
        else:
            # The team has not been assigned a coach yet
            team.coach_id = coach.coach_id
                        
    session.commit()
    print(f"Updated coaches for the {year} season")

session.close()