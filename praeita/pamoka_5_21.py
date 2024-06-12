# OPP principai

# Paveldėjimą

# class Tevas:
#     def __init_(self):
#         pass 
#     def atspausdink(self, tekstas):
#         print(tekstas)

# class Vaikas(Tevas):
#     pass


# tevas = Tevas()
# vaikas = Vaikas()

# tevas.atspausdink("Tekstas")
# vaikas.atspausdink("Tekstas")

# Polimorfizmą

# class Tevas:
#     def __init_(self):
#         pass 
#     def atspausdink(self, tekstas):
#         print(tekstas)

# class Vaikas(Tevas):
#     def atspausdink(self, tekstas):
#         print(f"****tekstas*****")


# tevas = Tevas()
# vaikas = Vaikas()

# tevas.atspausdink("Tekstas")
# vaikas.atspausdink("Tekstas")

# Abstrakciją - python neturim, jei nenaudojam package

# from abc import ABC, abstractmethod


# class Tevas(ABC):

#     @abstractmethod
#     def atspausdink(self, tekstas):
#         pass


# class Vaikas(Tevas):
#     def atspausdink(self, tekstas):
#         print(f"****{tekstas}*****")


# # tevas = Tevas()
# vaikas = Vaikas()

# # tevas.atspausdink("Tekstas")
# vaikas.atspausdink("Tekstas")

# Inkapsuliaciją

# # class Tevas:
#     def __init_(self):
#         self.tipas = "Geras"
#         self._vardas = "Jonas"
#         self.__asmens_kodas = 23156465665

#     def atspausdink(self, tekstas):
#         print(tekstas)

#     def _atspausdink_nevieša_info(self, tekstas):
#         print(tekstas)

#     def __atspausdink_privacia_info(self, tekstas):
#         print(tekstas)

#     def iskviesk(self, tekstas):
#         self.__atspausdink_privacia_info(tekstas)

# class Vaikas(Tevas):
#     def atspausdink(self, tekstas):
#         print(f"****tekstas*****")

#     def iskviesk(self, tekstas):
#         super()._atspausdink_nevieša_info(tekstas)


# tevas = Tevas()
# vaikas = Vaikas()

# tevas.atspausdink("Tekstas") # ok
# vaikas.atspausdink("Tekstas") # ok

# tevas._atspausdink_nevieša_info("Tekstas") # ne ok, neturetume taip iš čia kviesti protected
# tevas.__atspausdink_privacia_info("Tekstas") # ne ok, neturetume taip iš čia kviesti private

# tevas.iskviesk("tekstas")

# tevas.tipas = "kazkas"
# print(tevas.tipas)



class Irasas:
    def __init__(self, suma, tipas):
        self.suma = suma    
        self.tipas = tipas
        
    def __str__(self):
        return f'{self.tipas}: {self.suma}'
        
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma, 'Pajamos')
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info
        
    def __str__(self):
        return f'{self.tipas}: {self.suma}, Siuntejas: {self.siuntejas}, Info: {self.papildoma_info}'
    
class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma, 'Islaidos')
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        
    def __str__(self):
        return f'{self.tipas}: {self.suma} \nAtsiskaitymo budas: {self.atsiskaitymo_budas} \nPreke/Paslauga: {self.isigyta_preke_paslauga}'
    
    
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

    
kas = PajamuIrasas(20, 'tadas', 'ne')
print(kas)

x = Biudzetas()

x.prideti_pajamu_irasa(20, 'fsafa', 'safg')
x.ataskaita()
print(x)
