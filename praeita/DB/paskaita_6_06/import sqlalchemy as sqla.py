import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sqla.create_engine('sqlite:///mokykla.db')

Base = declarative_base()

class Knyga(Base):
    __tablename__ = 'Knygos'
    id = sqla.Column("Raktas", sqla.Integer, primary_key=True)
    pavadinimas = sqla.Column("Pavadinimas", sqla.String)
    autorius = sqla.Column("Autorius", sqla.String)
    
    def __init__(self, pavadinimas, autorius):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        
    def __repr__(self):
        return "<Knyga(pavadinimas='%s', autorius='%s')>" % (self.pavadinimas, self.autorius)
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

session.add(Knyga("Knyga1", "Autorius1"))

session.commit()

session.add(Knyga("Knyga2", "Autorius2"))

session.commit()

book = session.query(Knyga).all()
print(book)

book1 = session.query(Knyga).filter_by(id=2).first()
print(book1)