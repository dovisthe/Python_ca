class Transportas:
    def __init__(self, ratai, greitis, metai):
        self.ratai = ratai
        self.greitis = greitis
        if metai:
            self.metai = metai # optional , jei None prie metai naudoji
        
    def __str__(self):
        return f'Ratai : {self.ratai}, Greitis: {self.greitis}, Metai: {self.metai}'
        
    def vaziuoju(self):
        print("Wroommm wroomm")
        
class Motociklas(Transportas):
    def vaziuoju(self):
        print("Dziiuumm")
        
class Masina(Transportas):
    def __init__(self, ratai, greitis, metai, spalva):
            super().__init__(ratai, greitis, metai)
            self.spalva = spalva
        

    def __str__(self):
        return f'Ratai : {self.ratai}, Greitis: {self.greitis}, Metai: {self.metai}, Spalva: {self.spalva}'        

transporto_priemones = []
        
transportas = Transportas(4, 120, 1998)
motociklas = Motociklas(2, 280, 2005)
masina = Masina(4, 60, 2000, 'Juoda')


transporto_priemones.append(transportas)
transporto_priemones.append(motociklas)
transporto_priemones.append(masina)

for transporto_priemone_viena in transporto_priemones:
    print(transporto_priemone_viena)
    transporto_priemone_viena.vaziuoju()
    print()

# transportas.vaziuoju()
# motociklas.vaziuoju()
# masina.vaziuoju()


#ANTRAS VARIANTAS
