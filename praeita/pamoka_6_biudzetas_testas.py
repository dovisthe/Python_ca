
class Irasas:
    def __init__(self, suma):
        self.suma = suma    
        
    def __str__(self):
        return f' {self.suma}'
        
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info
        
    def __str__(self):
        return f'Pajamos: {self.suma}, Siuntejas: {self.siuntejas}, Info: {self.papildoma_info}'
    
class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        
    def __str__(self):
        return f'Islaidos: {self.suma}, Atsiskaitymo budas: {self.atsiskaitymo_budas}, Preke/Paslauga: {self.isigyta_preke_paslauga}'
   
class Biudzetas:
    def __init__(self):
        self.zurnalas = []
        self.balansas = 0
   
    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
        irasas = PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(irasas)
        self.balansas += suma
   
    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self.balansas -= suma
 
    def ataskaita(self):
        for irasas in self.zurnalas:    
            print(irasas)
        print(f'Balansas: {self.balansas}')
 
biudzetas = Biudzetas()
 
while True:
    pasirinkimas = input("Pasirinkite veiksma:\n1. Prideti pajamas\n2. Prideti islaidas\n3. Parodyti balansa\n4. Ataskaita\n5. Baigti\n")
   
    if pasirinkimas == "1":
        suma = float(input("Iveskite pajamas: "))
        siuntejas = input('Iveskite siunteja: ')
        papildoma_info = input('IVeskite papildoma info: ')
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)
   
    elif pasirinkimas == "2":
        suma = float(input("Iveskite islaidas: "))
        atsiskaitymo_budas = input('Iveskite atsiskaitymo buda: ')
        isigyta_preke_paslauga = input('Isigyta preke/paslauga: ')
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
 
    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.balansas}")
 
    elif pasirinkimas == "4":
        biudzetas.ataskaita()
 
    elif pasirinkimas == "5":
        print("Programa baige darba.")
        break
 
    else:
        print("Netinkamas pasirinkimas. Bandykite dar karta.")