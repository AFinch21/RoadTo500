from sqlalchemy import Column, Integer, Float, Date, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ExerciseLog(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'exercise_log'
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False) 
    date_yyyy_mm_dd = Column(Date)
    workout = Column(String)
    workout_name = Column(String)
    program_name = Column(String)
    body_weight_kg = Column(String)
    exercise = Column(String)
    setsreps = Column(String)
    setstime = Column(Float)
    top_set_repskg = Column(Float)
    e1rm_kg = Column(Float)
    reps = Column(Integer)
    volume_kg = Column(Integer)
    workout_volume_kg = Column(Integer)
    duration_hours = Column(Float)
    start_time_hmm = Column(Time)
    end_time_hmm = Column(Time)
    notes = Column(String)
    set_1_reps = Column(Integer)
    set_1_kg = Column(Float)
    set_2_reps = Column(Integer)
    set_2_kg = Column(Float)
    set_3_reps = Column(Integer)
    set_3_kg = Column(Float)
    set_4_reps = Column(Integer)
    set_4_kg = Column(Float)
    set_5_reps = Column(Integer)
    set_5_kg = Column(Float)