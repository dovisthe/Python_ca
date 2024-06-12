# class MyClass:
#     def __init__(self):
#         self.public = 'public'
#         self._protected = 'protected'
#         self.__private = 'private'
        
#     def kazkas(self):
#         print('hey')
         
# obj = MyClass()
# print(obj.public)
# print(obj._protected)
# print(obj.__private)

# obj.kazkas()
# class Suo:
#     def __init__(self, vardas, metus, asmens_kodas):
#         self.vardas = vardas
#         self.metus = metus
#         self.asmens_kodas = asmens_kodas
     
#     def vardas_didziosiomis(self):
#         return self.vardas.upper() 
        
#     def __str__(self):
#         return f'"Suns Vardas: {self.vardas}, metus: {self.metus}, asmens kodas {self.asmens_kodas}'

# class Person:
#     def __init__(self, vardas, metus, asmens_kodas):
#         self.vardas = vardas
#         self.metus = metus
#         self.asmens_kodas = asmens_kodas
     
#     def vardas_didziosiomis(self):
#         return self.vardas.upper() 
        
#     def __str__(self):
#         return f'"Vardas: {self.vardas}, metus: {self.metus}, asmens kodas {self.asmens_kodas}'
    
# zmogus1 = Person('Rokas', 1988, 84651654)
# zmogus2 = Person('Maikas', 1901, 245684651654)
# zmogus3 = Person('Lukas', 2021, 684651654)
# suo = Suo("Dog", 2023, 1007)

# print(zmogus1)
# print(zmogus2)
# print(suo)

# print(zmogus3.vardas_didziosiomis())
# print(zmogus3.metus)

#_____-----------------------------------------------------------
# Pirma uzduotis: sukurti klase Sakinys, kuri turi savybe tekstas ir metodus kurie:
#: grazina teksta atbulai

class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas
    
    def atspausdinti_atbulai(self):
        atbulas_tekstas = self.tekstas[::-1]
        print(atbulas_tekstas)
    
    def mazosiomis_raidem(self):
        mazosiomis_tekstas = self.tekstas.lower()
        print(mazosiomis_tekstas)
               
    def didziosiomis_raidem(self):
        didziosiomis_tekstas = self.tekstas.upper()
        print(didziosiomis_tekstas)
    
    def zodis_pagal_numeri(self, num):
        zodziai = self.tekstas.split()
        zodis_pagal_numeri = zodziai[num]
        print(zodis_pagal_numeri)

    def zodziu_kiekis(self):
        zdz_kiek = self.tekstas.strip().split()
        zodziu_sk = len(zdz_kiek)
        print(zodziu_sk)
        
    def simboliu_kiekis(self):
        simb_kiek = self.tekstas
        x = len(simb_kiek.replace(" ",""))
        print(x)
        
    # def zodzio_keitimas(self):
    #     x = input("Iveskite kuri norite pakeisti zodi: ")
    #     y = input("Iveskite kokiu zodziu norite pakeisti: ")
    #     sak = self.tekstas
    #     ats = sak.replace(x,y)
    #     print(ats)
 
    def skaiciu_counteris(self):
        skaic = 0
        txt = self.tekstas
        for sk in txt:
            if sk.isdigit():
                skaic += 1
        print(skaic)
    
   
    def viska_skaiciavimas(self):
        zdz_kiek = self.tekstas.strip().split()
        zodziu_sk = len(zdz_kiek)
        print(f'Sakinyje yra : {zodziu_sk} zodziai')
        skaic = 0
        txt = self.tekstas
        for sk in txt:
            if sk.isdigit():
                skaic += 1
        print(f'Sakinyje yra : {skaic} sakiciai')
        mazosios = 0
        for lwr in txt:
            if lwr.islower():
                mazosios += 1
        print(f'Sakinyje yra : {mazosios} mazosios')
        did = 0
        for upr in txt:
            if upr.isupper():
                did += 1
        print(f'Sakinyje yra : {did} didziosios')
    
        
        
        
               
sakinys1 = Sakinys('Miau Miau1 Miau2 Miau3 Au Au Au Au')

sakinys1.atspausdinti_atbulai()
sakinys1.mazosiomis_raidem()
sakinys1.didziosiomis_raidem()
sakinys1.zodis_pagal_numeri(1)
sakinys1.zodziu_kiekis()
sakinys1.simboliu_kiekis()
# sakinys1.zodzio_keitimas()
sakinys1.skaiciu_counteris()
sakinys1.viska_skaiciavimas()