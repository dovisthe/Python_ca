import os
from datetime import datetime

# antra skaidre

# pavadinimas = input("Parasykite failo pavadinima: ")
# with open(pavadinimas, 'a') as file:
#     while True:
#         x = input("Įveskite norimą tekstą: (enter sustabdys programa)")
#         file.write(x + "\n")
#         if x == "":
#             break
#         print(file.read()) 

failo_pavadinimas = input("Įveskite failo pavadinimą: ")
 
with open(failo_pavadinimas, 'w+', encoding='utf-8') as failas:
   
    print("Įveskite tekstą (tuščia eilutė baigia įvedimą):")
    while True:
        eilute = input()
        if eilute == "":
            break
        failas.write(eilute + "\n")
        failas.seek(0)
        print(failas.read())
print(f"Tekstas įrašytas į failą '{failo_pavadinimas}'")

# trecia skaidre

# # os.mkdir("C:\\Users\\dovis loptop\\Desktop\\Naujas aplankalas1")
# path = "C:\\Users\\dovis loptop\\Desktop\\Naujas aplankalas1\\failas.txt"
# with open(path, 'w') as file:
#     file.write(datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '\n')
# laikas = os.stat(path).st_ctime
# print(datetime.fromtimestamp(laikas))

# dydis = os.path.getsize(path)
# print(f'Dydis: {dydis}')

#ketvirta skaidre
# import pickle

# zurnalas = []

# while True:
#     pajamos = input("Iveskite pajamas(islaidas sy -): ")
#     if pajamos == "":
#         break
#     zurnalas.append(int(pajamos))
# print(zurnalas)

# with open('sarasas.pkl', 'wb') as pickle_out:
#     pickle.dump(zurnalas, pickle_out)
    
# with open('sarasas.pkl', 'rb') as pickle_in:
#     naujas_sarasas = pickle.load(pickle_in)
    
# print(naujas_sarasas)

# skaicius = 0
# for yrasas in naujas_sarasas:
#     skaicius += yrasas
# print(f'Balansas: {skaicius}')
