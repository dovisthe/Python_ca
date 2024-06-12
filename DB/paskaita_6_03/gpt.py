import sqlite3

conn = sqlite3.connect("mokykla.db")
c = conn.cursor()

c.execute('''
CREATE TABLE mokykla(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pavadinimas TEXT,
    destytojas TEXT,
    trukme INTEGER
)         
''')

conn.commit()

pavadinimas = "Vadyba"
destytojas = "Domantas"
trukme = 40
c.execute(f"INSERT INTO mokykla (pavadinimas, destytojas, trukme) VALUES ('{pavadinimas}', '{destytojas}', {trukme})")

pavadinimas2 = "Python"
destytojas2 = "Donatas"
trukme2 = 80
c.execute(f"INSERT INTO mokykla (pavadinimas, destytojas, trukme) VALUES ('{pavadinimas2}', '{destytojas2}', {trukme2})")

pavadinimas3 = "Java"
destytojas3 = "Tomas"
trukme3 = 80
c.execute(f"INSERT INTO mokykla (pavadinimas, destytojas, trukme) VALUES ('{pavadinimas3}', '{destytojas3}', {trukme3})")

c.execute('SELECT * FROM mokykla')
result = c.fetchall()
for student in result:
    print(student)
    
conn.close()