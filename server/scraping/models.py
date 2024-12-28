from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

# Define the Seasons table
class Season(Base):
    __tablename__ = 'seasons'
    __table_args__ = {'schema': 'coach_schema'}
    
    year = Column(Integer, primary_key=True)
    games_played = Column(Integer, nullable=False)

# Define the CoachData table
class CoachData(Base):
    __tablename__ = 'coach_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    coach_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    games = Column(Integer, default=0)
    wl_pct = Column(Float, default=0)

# Define the Teams table
class Team(Base):
    __tablename__ = 'teams'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    coach_id = Column(Integer, nullable=False, default=1)
    games = Column(Integer, nullable=False)
    extra_info = Column(JSONB, default={})  # Handling coaches who didn't last a full season

# Define the TotalOffensiveData table
class TotalOffensiveData(Base):
    __tablename__ = 'tot_off_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    pts_for = Column(Integer, default=0)
    yds = Column(Integer, default=0)
    plays = Column(Integer, default=0)
    ypp = Column(Float, default=0)  # yards per play
    turnovers = Column(Integer, default=0)
    penalties = Column(Integer, default=0)
    pen_yds = Column(Integer, default=0)
    firstd = Column(Integer, default=0)

# Define the PassingOffensiveData table
class PassingOffensiveData(Base):
    __tablename__ = 'pass_off_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    completions = Column(Integer, default=0)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    nya = Column(Float, default=0)  # Net yards per passing attempt
    first_downs = Column(Integer, default=0)

# Define the RushingOffensiveData table
class RushingOffensiveData(Base):
    __tablename__ = 'rush_off_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    ypa = Column(Float, default=0)  # yards per attempt
    first_downs = Column(Integer, default=0)

# Define the TotalDefensiveData table
class TotalDefensiveData(Base):
    __tablename__ = 'tot_def_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    pa = Column(Integer, default=0)  # Points Allowed
    yds = Column(Integer, default=0)
    plays = Column(Integer, default=0)
    ypp = Column(Float, default=0)  # yards per play
    turnovers = Column(Integer, default=0)
    penalties = Column(Integer, default=0)
    pen_yds = Column(Integer, default=0)
    firstd = Column(Integer, default=0)

# Define the PassingDefensiveData table
class PassingDefensiveData(Base):
    __tablename__ = 'pass_def_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    completions = Column(Integer, default=0)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    nya = Column(Float, default=0)  # Net yards per passing attempt
    first_downs = Column(Integer, default=0)

# Define the RushingDefensiveData table
class RushingDefensiveData(Base):
    __tablename__ = 'rush_def_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, primary_key=True)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    ypa = Column(Float, default=0)  # yards per attempt
    first_downs = Column(Integer, default=0)
