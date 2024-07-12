from database import get_db
from datetime import datetime
from Models.Darbuotojas import Darbuotojas
from Models.Departamentas import Departamentas
from Models.Projektas import Projektas

session = get_db()


def create_new_user(session):
    name = input("Iveskite varda: ")
    surname = input("Iveskite pavarde: ")
    
    birth_str = input('Įveskite gimimo datą (YYYY-MM-DD): ')
    birth = datetime.strptime(birth_str, '%Y-%m-%d')
    
    job_type = input("Iveskite darbo pareigas: ")
    salary = int(input("Iveskite atlyginima: "))    
    user = Darbuotojas(name, surname, birth, job_type, salary)
    session.add(user)
    session.commit()
    print("Naujas vartotojas sukurtas sėkmingai.")

def print_all_users(session):
    darbuotojai = session.query(Darbuotojas).all()
    for darbuotojas in darbuotojai:
        print(darbuotojas)

def delete_user(session):
    darbuotojai = session.query(Darbuotojas).all()
    for darbuotojas in darbuotojai:
        print(darbuotojas)
    id = int(input("Pasirinkite vartotojo id, kuri norite istrinti: "))
    user = session.get(Darbuotojas, id)
    session.delete(user)
    session.commit()
    print(f"Vartotojas su ID {id} ištrintas sėkmingai.")

def update_user(session):
    darbuotojai = session.query(Darbuotojas).all()
    for darbuotojas in darbuotojai:
        print(darbuotojas)
    id = int(input("Pasirinkite vartotojo id, kuri norite atnaujinti: "))
    user = session.get(Darbuotojas, id)
    pasirinkimas_keisti = int(input('''
Ka norite keisti?
1. Vardas
2. Pavarde
3. Gimimo data
4. Darbo pareigos
5. Atlyginimas
6. Kada pradejo
'''))
    if pasirinkimas_keisti == 1:
        new_name = input("Iveskite varda: ")
        user.name = new_name
    elif pasirinkimas_keisti == 2:
        new_surname = input("Iveskite pavarde: ")
        user.surname = new_surname
    elif pasirinkimas_keisti == 3:
        new_birth_str = input('Įveskite gimimo datą (YYYY-MM-DD): ')
        new_birth = datetime.strptime(new_birth_str, '%Y-%m-%d')
        user.birth = new_birth
    elif pasirinkimas_keisti == 4:
        new_job_type = input("Iveskite darbo pareigas: ")
        user.job_type = new_job_type
    elif pasirinkimas_keisti == 5:
        new_salary = int(input("Iveskite atlyginima: "))
        user.salary = new_salary
    elif pasirinkimas_keisti == 6:
        new_date_started_str = input("Įveskite kada pradėjo dirbti (YYYY-MM-DD): ")
        new_date_started = datetime.strptime(new_date_started_str, '%Y-%m-%d')
        user.date_started = new_date_started
    session.commit()
    
#------departamentas----------------------------    


    
def create_new_department(session):
    name = input("Iveskite departamento pavadinima: ")
    department = Departamentas(name)
    session.add(department)
    session.commit()
    print("Naujas departamentas sukurtas sėkmingai.")


def print_all_departments():
    departamentas = session.query(Departamentas).all()
    return departamentas
        
def add_darbuotojas_to_departmentas(darbuotojas_id, departamentas_id):
    darbuotojas = session.get(Darbuotojas, darbuotojas_id)
    departamentas = session.get(Departamentas, departamentas_id)
    session.add(departamentas)
    session.add(darbuotojas)
    
    if darbuotojas and departamentas:
        darbuotojas.departamentas = departamentas
        session.commit()
        print("Darbuotojas pridėtas sėkmingai.")
        
def delete_departamentas(id):
    departamentas = session.query(Departamentas).all()
    id = int(input("Pasirinkite departamento id, kuri norite istrinti: "))
    departamentas = session.get(Departamentas, id)
    session.delete(departamentas)
    session.commit()
    print(f"Departamentas su ID {id} ištrintas sėkmingai.")
        
        
#------------projektai---------------

def create_projektas(name):
    name = input("projekto pavadinima: ")
    projektas = Projektas(name)

    session.add(projektas)
    session.commit()

def get_all_projektai():
    projektas = session.query(Projektas).all()
    return projektas       
    
def add_darbuotojas_to_projektas(darbuotojas_id, projektas_id):
    darbuotojas = session.get(Darbuotojas, darbuotojas_id)# gets the user by id
    projektas = session.get(Projektas, projektas_id)# gets the role by id
    session.add(darbuotojas)
    session.add(projektas)

    if darbuotojas and projektas: # check if not None
        darbuotojas.projektai.append(projektas)# we append role to user roles list
        session.commit()
        
# def add_darbuotojas_to_projektas(darbuotojas_id, projektas_id):?????????????????????????????????ar veikia? TODO
#     darbuotojas = session.query(Darbuotojas).get(darbuotojas_id)
#     projektas = session.query(Projektas).get(projektas_id)
 
#     if darbuotojas and projektas:
#         darbuotojas.projektas = projektas
#         session.commit()
#         print("Darbuotojas sekmingai pridetas.")        
        
def delete_projektas(id):
    projektas = session.query(Projektas).all()
    id = int(input("Pasirinkite projekto id, kuri norite istrinti: "))
    projektas = session.get(Projektas, id)
    session.delete(projektas)
    session.commit()
    print(f"Projektas su ID {id} ištrintas sėkmingai.")