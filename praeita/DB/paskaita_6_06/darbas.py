import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sqla.create_engine('sqlite:///mokykla.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column("Name",sqla.String,)
    last_name = sqla.Column("Last_Name",sqla.String)
    age = sqla.Column("Age",sqla.Integer)
    
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        return f"{self.name}|{self.last_name}"    
        
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine) #priskiriame kelia

session = Session() # sakome pradeti darba 


person = User("dovis", "eidikis", "29")

session.add(person)

session.commit()

people = session.query(User).all()

print(people)