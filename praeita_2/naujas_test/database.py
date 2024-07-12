from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///naujas_test/Database/Vartotojai_Database2.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


_sessionMaker = sessionmaker(bind = engine)

def get_db():
    session = _sessionMaker()
    return session
