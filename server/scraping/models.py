from sqlalchemy import ForeignKeyConstraint, UniqueConstraint, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

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
    year = Column(Integer, ForeignKey('coach_schema.seasons.year'), nullable=False)
    coach_id = Column(Integer, ForeignKey('coach_schema.coach_data.coach_id'), nullable=False)
    games = Column(Integer, nullable=False)
    extra_info = Column(JSONB, default={})  # Handling coaches who didn't last a full season
    __table_args__ = (ForeignKeyConstraint(['year', 'coach_id'], ['coach_schema.seasons.year', 'coach_schema.coach_data.coach_id']),)
    __table_args__ = (UniqueConstraint('team_name', 'year', name='unique_team_year'),)

    # Relationships
    season = relationship("Season", backref="teams")
    coach = relationship("CoachData", backref="teams")

# Define the TotalOffensiveData table
class TotalOffensiveData(Base):
    __tablename__ = 'tot_off_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, ForeignKey('coach_schema.teams.team_id'), primary_key=True)
    pts_for = Column(Integer, default=0)
    yds = Column(Integer, default=0)
    plays = Column(Integer, default=0)
    ypp = Column(Float, default=0)  # yards per play
    turnovers = Column(Integer, default=0)
    penalties = Column(Integer, default=0)
    pen_yds = Column(Integer, default=0)
    firstD = Column(Integer, default=0)

    # Relationships
    team = relationship("Team", backref="total_offensive_data")

# Define the PassingOffensiveData table
class PassingOffensiveData(Base):
    __tablename__ = 'pass_off_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, ForeignKey('coach_schema.teams.team_id'), primary_key=True)
    completions = Column(Integer, default=0)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    nya = Column(Float, default=0)  # Net yards per passing attempt
    first_downs = Column(Integer, default=0)

    # Relationships
    team = relationship("Team", backref="passing_offensive_data")

# Define the RushingOffensiveData table
class RushingOffensiveData(Base):
    __tablename__ = 'rush_off_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, ForeignKey('coach_schema.teams.team_id'), primary_key=True)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    ypa = Column(Float, default=0)  # yards per attempt
    first_downs = Column(Integer, default=0)

    # Relationships
    team = relationship("Team", backref="rushing_offensive_data")

# Define the TotalDefensiveData table
class TotalDefensiveData(Base):
    __tablename__ = 'tot_def_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, ForeignKey('coach_schema.teams.team_id'), primary_key=True)
    pa = Column(Integer, default=0)  # Points Allowed
    yds = Column(Integer, default=0)
    plays = Column(Integer, default=0)
    ypp = Column(Float, default=0)  # yards per play
    turnovers = Column(Integer, default=0)
    penalties = Column(Integer, default=0)
    pen_yds = Column(Integer, default=0)
    firstD = Column(Integer, default=0)

    # Relationships
    team = relationship("Team", backref="total_defensive_data")

# Define the PassingDefensiveData table
class PassingDefensiveData(Base):
    __tablename__ = 'pass_def_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, ForeignKey('coach_schema.teams.team_id'), primary_key=True)
    completions = Column(Integer, default=0)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    nya = Column(Float, default=0)  # Net yards per passing attempt
    first_downs = Column(Integer, default=0)

    # Relationships
    team = relationship("Team", backref="passing_defensive_data")

# Define the RushingDefensiveData table
class RushingDefensiveData(Base):
    __tablename__ = 'rush_def_data'
    __table_args__ = {'schema': 'coach_schema'}
    
    team_id = Column(Integer, ForeignKey('coach_schema.teams.team_id'), primary_key=True)
    attempts = Column(Integer, default=0)
    yards = Column(Integer, default=0)
    touchdowns = Column(Integer, default=0)
    ypa = Column(Float, default=0)  # yards per attempt
    first_downs = Column(Integer, default=0)

    # Relationships
    team = relationship("Team", backref="rushing_defensive_data")
