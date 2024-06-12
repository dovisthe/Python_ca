#pirma skaidre


# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas
        
#     def __str__(self):
#         return f'Auto metai: {self.metai}, \nauto modelis: {self.modelis}, \nkuro tipas: {self.kuro_tipas}'
        
#     def vaziuoti(self):
#         print('Vaziuoja')
        
#     def stoveti(self):
#         print('Priparkuota')
        
#     def pildyti_degalu(self):
#         print('Degalai ipilti')

# class Elektromobilis(Automobilis):
#     def pildyti_degalu(self):
#         print('Baterija ikrauta')
    
#     def vaziuoti_autonomiskai(self):
#         print('vaziuoja autonomiskai')
        
# bmw = Automobilis(2011, 'e91', 'dyzelinas')
# tesla = Elektromobilis(2020, "S", 'Elektra')

# print(bmw)
# bmw.vaziuoti()
# bmw.pildyti_degalu()
# bmw.stoveti()
# print(tesla)
# tesla.vaziuoti_autonomiskai()
# tesla.vaziuoti()
# tesla.pildyti_degalu()
# tesla.stoveti()


#Antra skaidre ----------------------------------------------------------------
import datetime as dt

# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = dt.datetime.strptime(dirba_nuo, "%Y-%m-%d")
        
#     def _kiek_nudirbo_nuo_datos(self):
#         dabar = dt.datetime.now()
#         dirba_laiko = dabar - self.dirba_nuo
#         return dirba_laiko.days

#     def paskaiciuoti_atlyginima(self):
#         darbo_dienos = self._kiek_nudirbo_nuo_datos()
#         valandos = darbo_dienos * 8
#         atlyginimas = valandos * self.valandos_ikainis
#         return atlyginimas
        
        
# class NormalusDarbuotojas(Darbuotojas):
#     def _kiek_nudirbo_nuo_datos(self):
#         dabar = dt.datetime.now()
#         dirba_laiko = dabar - self.dirba_nuo
#         bendra_sav_kiekis = dirba_laiko.days // 7
#         extra_dienos = bendra_sav_kiekis % 7
#         darbo_dienos = bendra_sav_kiekis * 5
#         if extra_dienos > 5:
#             darbo_dienos += 5
#         else:
#             darbo_dienos += extra_dienos
#         return darbo_dienos
    
# jonas = Darbuotojas("Jonas", 10, '2024-1-10')    
# print(jonas.paskaiciuoti_atlyginima())    

# petras = NormalusDarbuotojas("Petras", 10, '2024-1-10')    
# print(petras.paskaiciuoti_atlyginima())    



#Trecia uzduotis------------------------------------------------------------------------------------
        
#------------------------------------------------------------------------       
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