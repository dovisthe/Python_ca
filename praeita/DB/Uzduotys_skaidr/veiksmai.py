from Klasses.Darbuotojas import Darbuotojas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import functions.views as p
import tkinter as tk

def main():
    engine = create_engine('sqlite:///Uzduotys_skaidr/Databases/Darbuotojas_Database.db')
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()

    def create_new_user():
        result = p.create_new_user(
            session,
            name_entry.get().strip(),
            surname_entry.get().strip(),
            birth_entry.get().strip(),
            job_entry.get().strip(),
            salary_entry.get().strip(),
        )
        status_label.config(text=result, fg="green")

    def print_all_users():
        result = p.print_all_users(session)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

    def delete_user():
        user_id = int(delete_id_entry.get().strip())
        result = p.delete_user(session, user_id)
        status_label.config(text=result, fg="green")

    def update_user():
        user_id = int(update_id_entry.get().strip())
        choice = int(update_choice_entry.get().strip())
        new_value = new_value_entry.get().strip()
        result = p.update_user(session, user_id, choice, new_value)
        status_label.config(text=result, fg="green")

    root = tk.Tk()
    root.title("Employee Management System")

    # Create labels and entries for input
    tk.Label(root, text="Vardas:").grid(row=0, column=0)
    tk.Label(root, text="Pavardė:").grid(row=1, column=0)
    tk.Label(root, text="Gimimo data (YYYY-MM-DD):").grid(row=2, column=0)
    tk.Label(root, text="Darbo pareigos:").grid(row=3, column=0)
    tk.Label(root, text="Atlyginimas:").grid(row=4, column=0)
    tk.Label(root, text="Pradėjo dirbti (YYYY-MM-DD):").grid(row=5, column=0)

    name_entry = tk.Entry(root)
    surname_entry = tk.Entry(root)
    birth_entry = tk.Entry(root)
    job_entry = tk.Entry(root)
    salary_entry = tk.Entry(root)
    date_started_entry = tk.Entry(root)

    name_entry.grid(row=0, column=1)
    surname_entry.grid(row=1, column=1)
    birth_entry.grid(row=2, column=1)
    job_entry.grid(row=3, column=1)
    salary_entry.grid(row=4, column=1)
    date_started_entry.grid(row=5, column=1)

    # Create buttons for actions
    create_button = tk.Button(root, text="Sukurti", command=create_new_user)
    create_button.grid(row=6, column=0, columnspan=2, pady=10)

    print_button = tk.Button(root, text="Spausdinti vartotojus", command=print_all_users)
    print_button.grid(row=7, column=0, columnspan=2, pady=10)

    # Create text widget to display results
    result_text = tk.Text(root, height=10, width=50)
    result_text.grid(row=8, column=0, columnspan=2, pady=10)

    # Create delete section
    tk.Label(root, text="Ištrinti vartotoją (Įveskite ID):").grid(row=9, column=0)
    delete_id_entry = tk.Entry(root)
    delete_id_entry.grid(row=9, column=1)
    delete_button = tk.Button(root, text="Ištrinti", command=delete_user)
    delete_button.grid(row=10, column=0, columnspan=2, pady=10)

    # Create update section
    tk.Label(root, text="Atnaujinti vartotoją (Įveskite ID):").grid(row=11, column=0)
    update_id_entry = tk.Entry(root)
    update_id_entry.grid(row=11, column=1)
    tk.Label(root, text="Pasirinkimas (1-6):").grid(row=12, column=0)
    update_choice_entry = tk.Entry(root)
    update_choice_entry.grid(row=12, column=1)
    tk.Label(root, text="Nauja reikšmė:").grid(row=13, column=0)
    new_value_entry = tk.Entry(root)
    new_value_entry.grid(row=13, column=1)
    update_button = tk.Button(root, text="Atnaujinti", command=update_user)
    update_button.grid(row=14, column=0, columnspan=2, pady=10)

    # Status label
    status_label = tk.Label(root, text="")
    status_label.grid(row=15, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()