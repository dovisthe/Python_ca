
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to the root page!"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/contact")
def contact():
    return "This is the contact page."

@app.route("/<name>")
def print_name(name):
    return f"Labas, {name}!"

@app.route("/vartotojai/<user_id>")
def id_print(user_id):
    return f"Vartotojo id yra: {user_id}"

@app.route("/vardai")
def vardai():
    vardai = ["Rokas", "Tomas", "Paulius", "Diana"]
    return render_template("vardai.html", sarasas = vardai)


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("pasisveikinimas.html", vardas = vardas)
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.run()