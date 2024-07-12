from database import db
from Models.Vartotojas import Vartotojas
from Models.Masina import Masina




def sukurti_vartotoja(name):
    vartotojas = Vartotojas(name)
    db.session.add(vartotojas)
    db.session.commit()

def gauti_vartotojus():
    vartotojas = db.session.query(Vartotojas).all()
    return vartotojas

def gauti_vartotoja(id):
    vartotojas = db.session.get(Vartotojas, id)
    return vartotojas

def istrinti_vartotoja(id):
    vartotojas = gauti_vartotoja(id)
    db.session.delete(vartotojas)
    db.session.commit()

def atnaujinti_vartotoja(id, name):
    vartotojas = gauti_vartotoja(id)
    vartotojas.name = name
    db.session.commit()
    
def add_masina_to_vartotojas(masina_id, vartotojas_id):
    vartotojas = db.session.get(Vartotojas, vartotojas_id)
    masina = db.session.get(Masina, masina_id)
    
    if vartotojas and masina:
        vartotojas.masinos.append(masina)
        db.session.commit()
        print("masina pridėta sėkmingai.")