from datetime import datetime
from Klasses.Darbuotojas import Darbuotojas
from sqlalchemy import create_engine


def create_new_user(session, name, surname, birth_str, job_type, salary):
    try:
        birth = datetime.strptime(birth_str, '%Y-%m-%d')
        
        new_user = Darbuotojas(name, surname, birth, job_type, int(salary))
        session.add(new_user)
        session.commit()
        return "Naujas vartotojas sukurtas sėkmingai."
    except ValueError as ve:
        return f"Įvesties klaida: {ve}"
    except Exception as e:
        return f"Klaida kuriant vartotoją: {e}"

def print_all_users(session):
    darbuotojai = session.query(Darbuotojas).all()
    return "\n".join(str(darbuotojas) for darbuotojas in darbuotojai)

def delete_user(session, user_id):
    try:
        user = session.get(Darbuotojas, user_id)
        session.delete(user)
        session.commit()
        return f"Vartotojas su ID {user_id} ištrintas sėkmingai."
    except Exception as e:
        return f"Klaida ištrinant vartotoją: {e}"

def update_user(session, user_id, choice, new_value):
    try:
        user = session.get(Darbuotojas, user_id)
        if choice == 1:
            user.name = new_value
        elif choice == 2:
            user.surname = new_value
        elif choice == 3:
            user.birth = datetime.strptime(new_value, '%Y-%m-%d')
        elif choice == 4:
            user.job_type = new_value
        elif choice == 5:
            user.salary = int(new_value)
        elif choice == 6:
            user.date_started = datetime.strptime(new_value, '%Y-%m-%d')
        session.commit()
        return "Vartotojo duomenys atnaujinti sėkmingai."
    except ValueError as ve:
        return f"Įvesties klaida: {ve}"
    except Exception as e:
        return f"Klaida atnaujinant vartotoją: {e}"