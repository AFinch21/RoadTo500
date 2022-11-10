from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.orm import ExerciseLog
import pandas as pd

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/Andrew')
Base.metadata.create_all(engine)
file_name = r'/Users/Andrew/Development/2. Software Development/2. Apps/Road To 500/road-to-500/Data_ETL/Data/StrongLifts20221108.csv'
df = pd.read_csv(file_name)

df.to_sql(con=engine, index_label='id', name=ExerciseLog.__tablename__, if_exists='replace')
