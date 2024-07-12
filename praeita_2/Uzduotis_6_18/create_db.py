from database import db, app
from Models.Vartotojas import Vartotojas
from Models.Masina import Masina

with app.app_context():
    db.create_all()

    dzonis = Vartotojas("Dzonis")
    jaze = Vartotojas("Jaze")
    maikas = Vartotojas("Maikas")

    db.session.add_all([dzonis, jaze, maikas])
    
    bmw = Masina("BMW")
    vw = Masina("VW")
    tesla = Masina("Tesla")
    
    db.session.add_all([bmw,vw,tesla])
    db.session.commit()

