from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .associations import darb_projekt_associasion
from ..database import Base





class Projektas(Base):
    __tablename__ = "Projektas"

    id = Column(Integer, primary_key = True)
    projektas = Column(String)

    darbuotojas = relationship("Darbuotojas", secondary = darb_projekt_associasion, back_populates="projektai")# many to many Roles with Users


    def __init__(self, projektas):
        self.projektas = projektas

    def __repr__(self):
        return f"id: {self.id}, name: {self.projektas}"