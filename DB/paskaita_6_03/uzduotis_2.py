import sqlite3

conn = sqlite3.connect("mokykla.db")
c = conn.cursor()

# c.execute('''
# CREATE TABLE IF NOT EXISTS mokykla(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     pavadinimas TEXT,
#     destytojas TEXT,
#     trukme INTEGER
# )         
# ''')

# conn.commit()

# pavadinimas = "Vadyba"
# destytojas = "Domantas"
# trukme = 40
# c.execute(f"INSERT INTO mokykla (pavadinimas, destytojas, trukme) VALUES ('{pavadinimas}', '{destytojas}', {trukme})")

# pavadinimas2 = "Python"
# destytojas2 = "Donatas"
# trukme2 = 80
# c.execute(f"INSERT INTO mokykla (pavadinimas, destytojas, trukme) VALUES ('{pavadinimas2}', '{destytojas2}', {trukme2})")

# pavadinimas3 = "Java"
# destytojas3 = "Tomas"
# trukme3 = 80
# c.execute(f"INSERT INTO mokykla (pavadinimas, destytojas, trukme) VALUES ('{pavadinimas3}', '{destytojas3}', {trukme3})")
  
# conn.commit()

#########################################
print("Trukme >50")
with conn:
    c.execute('SELECT * FROM mokykla WHERE trukme > 50')
    result = c.fetchall()
    for laikas in result:
        print(laikas)

print()
###################################################


# c.execute('UPDATE mokykla SET pavadinimas = "Ziauriniai Python kursai" WHERE pavadinimas = "Python kursai"')
# conn.commit()


#################################
print("Istrinam Tomas")
# c.execute('DELETE FROM mokykla WHERE destytojas = "Tomas"')
# conn.commit()
print()
#######################################
print("visos paskaitos")
with conn:
    c.execute('SELECT * FROM mokykla')
    result = c.fetchall()
    for laikas in result:
        print(laikas)
        
        

