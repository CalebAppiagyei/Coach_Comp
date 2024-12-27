import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, inspect, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
coach_url = os.getenv("COACH_PATH")
db_url = os.getenv("DB_URL")
engine = create_engine(db_url, echo=True)
# inspector = inspect(engine)
Base = declarative_base()

# tables = inspector.get_table_names(schema='coach_schema')
# for table in tables:
#     print(table)

# Defining the Coach table
class Coach(Base):
    __tablename__ = 'coach_data'
    __table_args__ = {'schema': 'coach_schema'}
    coach_id = Column(Integer, primary_key=True)
    name = Column(String)
    games = Column(Integer)
    wl_pct = Column(Float)
    
# Creating the session
Session = sessionmaker(bind=engine)
session = Session()

years = range(2000, 2024)
for year in years:
    # Formatting the coach table
    coaches = pd.read_csv(coach_url + "/{}.csv".format(year), header=1)
    coaches = coaches[["Coach", "G.2", "W.2", "L.2", "T.2"]]
    coaches['wl_pct'] = (coaches['W.2'] + (coaches['T.2'] * 0.5)) / coaches['G.2']

    for index, row in coaches.iterrows():
        # Inserting each coach into the table
        new_coach = Coach(name=row['Coach'], games=row['G.2'], wl_pct=row['wl_pct'])
        
        # Checking for duplicates
        check_dup = session.query(Coach).filter(Coach.name == row['Coach'], Coach.games == row['G.2'], Coach.wl_pct == row['wl_pct']).first()
        if not check_dup:
            session.add(new_coach)
        
    session.commit()

session.close()