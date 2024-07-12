from Models.Vartotojas import Vartotojas
from Models.Masina import Masina
from database import db

 
def sukurti_masina(name):
    masina = Masina(name)
    db.session.add(masina)
    db.session.commit()

def gauti_masinas():
    masina = db.session.query(Masina).all()
    return masina

def gauti_masina(id):
    masina = db.session.get(Masina, id)
    return masina

def istrinti_masina(id):
    masina = db.session.get(Masina, id)
    db.session.delete(masina)
    db.session.commit()

def atnaujinti_masina(id, name):
    masina = db.session.get(Masina, id)
    masina.name = name
    db.session.commit()
    
def skaiciuoti_masinas():
    count = db.session.query(Masina).count()
    return count