from modules.biudzetas import biudzetas as b


while True:
    pasirinkimas = input("Pasirinkite veiksma:\n1. Prideti pajamas\n2. Prideti islaidas\n3. Parodyti balansa\n4. Ataskaita\n5. Baigti\n")
   
    if pasirinkimas == "1":
        suma = float(input("Iveskite pajamas: "))
        siuntejas = input('Iveskite siunteja: ')
        papildoma_info = input('IVeskite papildoma info: ')
        b.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)
   
    elif pasirinkimas == "2":
        suma = float(input("Iveskite islaidas: "))
        atsiskaitymo_budas = input('Iveskite atsiskaitymo buda: ')
        isigyta_preke_paslauga = input('Isigyta preke/paslauga: ')
        b.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
 
    elif pasirinkimas == "3":
        print(f"Balansas: {b.balansas}")
 
    elif pasirinkimas == "4":
        b.ataskaita()
 
    elif pasirinkimas == "5":
        print("Programa baige darba.")
        break
 
    else:
        print("Netinkamas pasirinkimas. Bandykite dar karta.")
        