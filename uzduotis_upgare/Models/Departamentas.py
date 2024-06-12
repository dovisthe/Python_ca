from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base





class Departamentas(Base):
    __tablename__ = "Departamentas"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    name = Column(String)

    darbuotojas = relationship("Darbuotojas", back_populates="departamentas")  # one to many, one User has many Invoices


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"