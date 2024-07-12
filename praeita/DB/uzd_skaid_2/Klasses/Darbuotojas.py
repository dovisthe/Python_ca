import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///uzd_skaid_2/Databases/Darbuotojas_Database.db')

Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'Darbuotojas'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth = Column(DateTime)
    job_type = Column(String)
    salary = Column(Integer)
    date_started = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, name, surname, birth, job_type, salary):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.job_type = job_type
        self.salary = salary
        
    def __repr__(self):
        return f"{self.id}|{self.name}|{self.surname}|{self.birth.date()}|{self.job_type}|{self.salary}|{self.date_started.date()}"
    
Base.metadata.create_all(engine)