from sqlalchemy import Column, Integer, Table, ForeignKey
from ..database import Base




darb_projekt_associasion = Table(
    "darbuotojai_projektai", # table name
    Base.metadata, # Base inheritange
    Column('darbuotojas_id', Integer, ForeignKey('Darbuotojas.id')),
    Column('projektas_id', Integer, ForeignKey('Projektas.id'))
)


