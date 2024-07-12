from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///uzduotis_upgare/Database/Vartotojai_Database2.db')


Base = declarative_base()

_sessionMaker = sessionmaker(bind = engine)

def get_db():
    session = _sessionMaker()
    return session
