from Models.Vartotojas import Vartotojas
from database import db

def gauti_sarasa():
    vartotojai = db.session.query(Vartotojas).all()
    return vartotojai

