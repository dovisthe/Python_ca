import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .associations import darb_projekt_associasion
from ..database import Base
from . import Projektas
from . import Departamentas


class Darbuotojas(Base):
    __tablename__ = 'Darbuotojas'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth = Column(DateTime)
    job_type = Column(String)
    salary = Column(Integer)
    date_started = Column(DateTime, default=datetime.datetime.utcnow)
    departamentas_id = Column(Integer, ForeignKey('Departamentas.id'))
    
    
    projektai = relationship("Projektas", secondary=darb_projekt_associasion, back_populates="darbuotojas")
        
    departamentas = relationship("Departamentas", back_populates="darbuotojas")
    
    def __init__(self, name, surname, birth, job_type, salary):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.job_type = job_type
        self.salary = salary
        
    def __repr__(self):
        return f"{self.id}|{self.name}|{self.surname}|{self.birth.date()}|{self.job_type}|{self.salary}|{self.date_started.date()}"
