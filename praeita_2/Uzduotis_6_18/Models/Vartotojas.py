from database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Vartotojas(db.Model):
    __tablename__ = "Vartotojas"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)


    masinos = relationship("Masina", back_populates="vartotojas")

    def __init__(self, name):
        self.name = name
