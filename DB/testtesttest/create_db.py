from database import Base, engine
import Models.Darbuotojas


print("Started creating database")
Base.metadata.create_all(engine)
print("Finished creating database")