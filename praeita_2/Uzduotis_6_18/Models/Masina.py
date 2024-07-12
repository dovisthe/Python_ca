from database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Masina(db.Model):
    __tablename__ = "Masina"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    vartotojas_id = Column(Integer, ForeignKey('Vartotojas.id'))
    modelis = db.Column(db.String)

    vartotojas = relationship("Vartotojas", back_populates="masinos")

    def __init__(self, name):
        self.name = name
