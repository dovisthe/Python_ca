from database import Base, engine
from Models.Darbuotojas import Darbuotojas
from Models.Departamentas import Departamentas
from Models.Projektas import Projektas


print("Started creating database")
Base.metadata.create_all(engine)
print("Finished creating database")