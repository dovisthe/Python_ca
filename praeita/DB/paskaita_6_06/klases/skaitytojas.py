import pickle


class Skaitytojas:
    def __init__(self, vardas, pasiskolintos_failas='sar.pkl'):
        self.vardas = vardas
        self.pasiskolintos_knygos = []
        self.pasiskolintos_failas = pasiskolintos_failas
        
    def pasiskolinti_knyga(self, knyga, data_iki_kada):
        if any(knyga.ar_veluojama() for knyga in self.pasiskolintos_knygos):
            print("Turite negrąžintų knygų")
            return False
        if knyga.ar_paimta:
            print(f"Knyga '{knyga.pavadinimas}' negalima pasiskolinti, knyga paimta")
            return False 
        knyga.pasiskolinti(data_iki_kada)
        self.pasiskolintos_knygos.append(knyga)
        self.issaugoti_knyga()
        return True

    def grazinti_knyga(self, knyga, biblioteka):
        if knyga in self.pasiskolintos_knygos:
            self.pasiskolintos_knygos.remove(knyga)
            knyga.grazinti()
            biblioteka.issaugoti_knyga()
            print(f"Knyga '{knyga.pavadinimas}' grąžinta sėkmingai!")
            return True
        else:
            print(f"Knyga '{knyga.pavadinimas}' nėra pasiskolinta.")
            return False
        
    def uzkraut_pasiskolintas_knygas(self):
        try:
            with open(self.pasiskolintos_failas, 'rb') as file:
                self.pasiskolintos_knygos = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.pasiskolintos_knygos = []
            
    def issaugoti_knyga(self):
        with open(self.pasiskolintos_failas, 'wb') as file:
            pickle.dump(self.pasiskolintos_knygos, file)
    
    def ieskoti_knygos(self, ieskoti_pagal):
        return [knyga for knyga in self.pasiskolintos_knygos if ieskoti_pagal.lower() in knyga.pavadinimas.lower() or ieskoti_pagal.lower() in knyga.autorius.lower()]