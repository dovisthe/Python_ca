from crud import *



def main():

    while True:
        pasirinkimas = input(
            '''
1. Sukurk nauja vartotoja
2. Atspausdink visus vartotojus
3. Istrinti vartotoja
4. Atnaujinti vartotoja
5. sukurti departamenta
6. pridet vartotoja prie departamento
7. sukurti projekta
8. prideti darbuotoja prie projekto
9. Istrinti projekta
10. istrinti departamenta
11. Baigti


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
            create_new_department(session)
        elif pasirinkimas == "6":
            id = int(input("Iveskite darbuotojas id: "))
            id2 = int(input("Iveskite departamentas id: "))
            add_darbuotojas_to_departmentas(id, id2)
        elif pasirinkimas == "7":
            create_projektas(session)
        elif pasirinkimas == "8":
            user_id = input("Įveskite darbuotojo id: ")
            role_id = input("Įveskite projekto id: ")
            add_darbuotojas_to_projektas(user_id, role_id)   
        elif pasirinkimas == "9":
            delete_projektas(session)     
        elif pasirinkimas == "10":
            delete_departamentas(session)
        elif pasirinkimas == "11":
            break


if __name__ == "__main__":
    main()