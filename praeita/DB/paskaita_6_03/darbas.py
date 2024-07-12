import sqlite3

conn = sqlite3.connect("students.db")

c = conn.cursor()

# c.execute('''
# DROP TABLE students       
# ''')
# conn.commit()


c.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)                    
''')
conn.commit()

while True:
    print("Iveskite studenta: ")
    name = input("Iveskite studento varda: ")
    age = int(input("Iveskite studento amziu: "))
    course = input("Iveskite studento kursa: ")
    
    with conn:
        c.execute(f"INSERT INTO students (name, age, course) VALUES ('{name}', {age}, '{course}')")
        
    print()
    
    with conn:
        c.execute('SELECT * FROM students')
        result = c.fetchall()
        for student in result:
            print(student)
            
    print()
