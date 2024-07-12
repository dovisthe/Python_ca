from flask import Flask, render_template, request
from leap_year import get_leap_years, is_leap_year
from database import app
from crud1 import *
from masinu_crud import *
from vartotoju_crud import *


# app = Flask(__name__)

#http://127.0.0.1:5000
@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/<index>")
# def user(index):
#     return (f" *Labas, {index}* " ) * 5



@app.route("/kintamieji")
def show_leap_years():
    start_year = 1920
    end_year = 2100
    leap_years = get_leap_years(start_year, end_year)
    return render_template('kintamieji.html', start_year=start_year, end_year=end_year, leap_years=leap_years)
    
    

@app.route("/patikrinimas", methods = ["GET", "POST"])
def patikrinimas():
    if request.method == "POST":
        year = int(request.form["year"])
        if is_leap_year(year):
            return render_template("atsakymas.html", message = f"Jusu metai - {year} yra keliamieji")
        else:
            return render_template("atsakymas.html", message = f"Jusu metai - {year} yra nekeliamieji")
    else:
        return render_template("patikrinimas.html")
    
#MASINU --------------------------------------------------------------------
@app.route("/masina")
def masina():
    visi = gauti_masinas()
    return render_template("masina/index.html", sarasas = visi)

@app.route("/vartotojas")
def vartotojas():
    visi = gauti_vartotojus()
    return render_template("vartotojas/index.html", sarasas = visi)


@app.route("/vartotojas/create", methods = ["GET", "POST"])
def vartotojas_create():
    if request.method == "POST":
        name = request.form["vardas"]
        sukurti_vartotoja(name)
        return render_template("vartotojas/message.html", message = f"Sėkmingai sukurtas vartotojas - {name}")
    else:
        return render_template("vartotojas/create.html")
    

@app.route("/vartotojas/add_car/<vartotojas_id>", methods = ["GET", "POST"])
def prideti_masina_vartotojui(vartotojas_id):
    if request.method == "POST":
        masina_id = request.form["masina_id"]
        add_masina_to_vartotojas(masina_id, vartotojas_id)
        return render_template("vartotojas/message.html", message = f"Sėkmingai prideta masina prie vartotojo")
    else:
        return render_template("vartotojas/add_car.html", vartotojas_id = vartotojas_id)
    
    
@app.route("/masina/create", methods = ["GET", "POST"])
def masina_create():
    if request.method == "POST":
        name = request.form["masina"]
        sukurti_masina(name)
        return render_template("masina/message.html", message = f"Sėkmingai sukurtas masina {name}")
    else:
        return render_template("masina/create.html")
    
    
@app.route("/masina/delete/<id>", methods = ["GET", "POST"])
def masina_delete(id):
    masina = gauti_masina(id)
    if masina is None:
        return render_template("vartotojas/message.html", message = f"Nėra masinos su id - {id}")
    
    if request.method == "POST":
        istrinti_masina(id)
        return render_template("vartotojas/message.html", message = f"Sėkmingai ištrinta masina - {masina.name}")
    else:
        return render_template("masina/delete.html", masina = masina)
    

@app.route("/vartotojas/delete/<id>", methods = ["GET", "POST"])
def vartotojai_delete(id):
    vartotojas = gauti_vartotoja(id)
    if vartotojas is None:
        return render_template("vartotojas/message.html", message = f"Nėra vartotojo su id - {id}")
    
    if request.method == "POST":
        istrinti_vartotoja(id)
        return render_template("vartotojas/message.html", message = f"Sėkmingai ištrintas vartotojas - {vartotojas.name}")
    else:
        return render_template("vartotojas/delete.html",  vartotojas = vartotojas)


@app.route("/vartotojas/update/<id>", methods = ["GET", "POST"])
def vartotojai_update(id):
    vartotojas = gauti_vartotoja(id)
    if vartotojas is None:
        return render_template("vartotojas/message.html", message = f"Nėra vartotojo su id - {id}")
    
    if request.method == "POST":
        name = request.form["vardas"]
        atnaujinti_vartotoja(id, name)
        return render_template("vartotojas/message.html", message = f"Sėkmingai atnaujintas vartotojas - {vartotojas.name}")
    else:
        return render_template("vartotojas/update.html",  vartotojas = vartotojas) 


@app.route("/masina/update/<id>", methods = ["GET", "POST"])
def masina_update(id):
    masina = gauti_masina(id)
    if masina is None:
        return render_template("masina/message.html", message = f"Nėra vartotojo su id - {id}")
    
    if request.method == "POST":
        name = request.form["vardas"]
        atnaujinti_masina(id, name)
        return render_template("masina/message.html", message = f"Sėkmingai atnaujinta masina - {masina.name}")
    else:
        return render_template("masina/update.html",  masina = masina) 


if __name__ == '__main__':
    app.run(debug=True)

