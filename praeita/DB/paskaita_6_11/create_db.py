from database import Base, engine
import Models.Role 
import Models.User
import Models.Invoice


print("Started creating database")
Base.metadata.create_all(engine)
print("Finished creating")