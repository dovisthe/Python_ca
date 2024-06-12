from klases.knyga import Knyga
from klases.biblioteka import Biblioteka
from klases.skaitytojas import Skaitytojas
from datetime import datetime, timedelta

biblioteka = Biblioteka()

def pasirinkimai():
    print("\nBibliotekos valdymo sistema")
    print("1. Pridėti naują knygą")
    print("2. Pašalinti knygą")
    print("3. Ieškoti knygos")
    print("4. Peržiūrėti visų knygų sąrašą")
    print("5. Peržiūrėti neatneštų knygų sąrašą")
    print("6. Pasiskolinti knygą")
    print("7. Grąžinti knygą")
    print("0. Išeiti")

def pasirinkimas1():
    pavadinimas = input("Įveskite knygos pavadinimą: ")
    autorius = input("Įveskite knygos autorių: ")
    isleidimo_metai = int(input("Įveskite knygos išleidimo metus: "))
    zanras = input("Įveskite knygos žanrą: ")
    biblioteka.prideti_knyga(pavadinimas, autorius, isleidimo_metai, zanras)
    print("Knyga pridėta sėkmingai!")

def pasirinkimas2():
    isleidimo_metai = int(input("Įveskite knygos išleidimo metus, kurią norite pašalinti: "))
    biblioteka.pasalinti(isleidimo_metai)
    print("Knyga pašalinta sėkmingai!")

def pasirinkimas3():
    ieskoti_pagal = input("Įveskite paieškos frazę (pavadinimas ar autorius)(nieko nepasirinkus, rodys visas): ")
    rezultatai = biblioteka.ieskoti_knygos(ieskoti_pagal)
    if rezultatai:
        for knyga in rezultatai:
            print(f"Pavadinimas: {knyga.pavadinimas}, Autorius: {knyga.autorius}, Išleidimo metai: {knyga.isleidimo_metai}, Žanras: {knyga.zanras}")
    else:
        print("Knygų nerasta pagal paieškos kriterijus.")

def pasirinkimas4():
    knygos = biblioteka.knygu_sarasas()
    if knygos:
        for knyga in knygos:
            print(f"Pavadinimas: {knyga.pavadinimas}, Autorius: {knyga.autorius}, Išleidimo metai: {knyga.isleidimo_metai}, Žanras: {knyga.zanras}")
    else:
        print("Nerasta knygu")

def pasirinkimas5():
    neatnestos_knygos = biblioteka.neatnestu_knygu_sarasas()
    if neatnestos_knygos:
        for knyga in neatnestos_knygos:
            print(f"Pavadinimas: {knyga.pavadinimas}, Autorius: {knyga.autorius}, Išleidimo metai: {knyga.isleidimo_metai}, Žanras: {knyga.zanras}, Kada atiduoti: {knyga.kada_atiduoti}")
    else:
        print('nera knygu')

def pasirinkimas6():
    vardas = input("Įveskite savo vardą: ")
    skaitytojas = biblioteka.pridet_skaitytoja_prie_saraso(vardas)
    skaitytojas = Skaitytojas(vardas)
    pavadinimas = input("Įveskite knygos pavadinimą, kurią norite pasiskolinti: ")
    knygos = biblioteka.ieskoti_knygos(pavadinimas)
    if knygos:
        knyga = knygos[0]
        data_iki_kada = datetime.now().date() + timedelta(days=14)
        ar_pavyko_pasiskolinti = skaitytojas.pasiskolinti_knyga(knyga, data_iki_kada)
        if ar_pavyko_pasiskolinti:
            biblioteka.issaugoti_knyga()
            skaitytojas.issaugoti_knyga()
            print(f"Knyga '{knyga.pavadinimas}' pasiskolinta iki {data_iki_kada}")
    else:
        print("Knyga nerasta.")

def pasirinkimas7():
    vardas = input("Įveskite savo vardą: ")
    skaitytojas = biblioteka.pasalinti_sakitytoja(vardas)
    skaitytojas = Skaitytojas(vardas)  
    pavadinimas = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
    knygos = biblioteka.ieskoti_knygos(pavadinimas)
    if knygos:
        knyga = knygos[0]
        if knyga.ar_paimta:
            ar_pavyko = skaitytojas.grazinti_knyga(knyga, biblioteka)
            if ar_pavyko:
                biblioteka.issaugoti_knyga()
                skaitytojas.issaugoti_knyga()
                print(f"Knyga '{knyga.pavadinimas}' grąžinta sėkmingai!")
            else:
                print(f"Knyga '{knyga.pavadinimas}' negali būti grąžinta, nes jos nėra pasiskolinta.")
    else:
        print("Knyga nerasta.")


