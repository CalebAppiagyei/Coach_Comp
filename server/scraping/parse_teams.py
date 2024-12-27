import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, inspect, Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import JSONB
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


session.close()