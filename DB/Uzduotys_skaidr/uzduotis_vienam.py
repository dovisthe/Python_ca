from datetime import datetime
from Klasses.Darbuotojas import Darbuotojas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

def main():

    engine = create_engine('sqlite:///Uzduotys_skaidr/Databases/Darbuotojas_Database.db')
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()

    while True:
        pasirinkimas = input(
            '''
1. Sukurk nauja vartotoja
2. Atspausdink visus vartotojus
3. Istrinti vartotoja
4. Atnaujinti vartotoja
5. Baigti

Iveskite: '''
        )

        if pasirinkimas == "1":
            create_new_user(session)
        elif pasirinkimas == "2":
            print_all_users(session)
        elif pasirinkimas == "3":
            delete_user(session)
        elif pasirinkimas == "4":
            update_user(session)
        elif pasirinkimas == "5":
            break


if __name__ == "__main__":
    main()