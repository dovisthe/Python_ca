import pickle
if __name__ == "__main__":
    from knyga import Knyga
else:
    from klases.knyga import Knyga
    
if __name__ == "__main__":
    from skaitytojas import Skaitytojas
else:
    from klases.skaitytojas import Skaitytojas

class Biblioteka:
    def __init__(self, bibl_failas='biblioteka.pkl', sar_skaitytoju_failas='sar_skait.pkl'):
        self.bibl_failas = bibl_failas
        self.knygos = []
        self.uzkrauti_knygas()
        self.sar_skaitytoju = []
        self.sar_skaitytoju_failas = sar_skaitytoju_failas
        self.uzkrauti_skaitytojai()

    def uzkrauti_skaitytojai(self):
        try:
            with open(self.sar_skaitytoju_failas, 'rb') as file:
                self.sar_skaitytoju = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.sar_skaitytoju = []
            
    def issaugoti_skaitytoja(self):
        with open(self.sar_skaitytoju_failas, 'wb') as file:
            pickle.dump(self.sar_skaitytoju, file)

    def pridet_skaitytoja_prie_saraso(self, vardas):
        naujas_skaitytojas = Skaitytojas(vardas)
        self.sar_skaitytoju.append(naujas_skaitytojas)
        self.issaugoti_skaitytoja()
    
    def ieskoti_skaitytoja(self, ieskoti_pagal):
        return[skaitytojas for skaitytojas in self.sar_skaitytoju if ieskoti_pagal in skaitytojas.vardas()]
    
    def pasalinti_sakitytoja(self, vardas):
        for skaitytojas in self.sar_skaitytoju:
            if skaitytojas.vardas == vardas:
                self.sar_skaitytoju.remove(skaitytojas)
        return None
        
    def uzkrauti_knygas(self):
        try:
            with open(self.bibl_failas, 'rb') as file:
                self.knygos = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.knygos = []

    def issaugoti_knyga(self):
        with open(self.bibl_failas, 'wb') as file:
            pickle.dump(self.knygos, file)

    def prideti_knyga(self, pavadinimas, autorius, isleidimo_metai, zanras):
        nauja_knyga = Knyga(pavadinimas, autorius, isleidimo_metai, zanras)
        self.knygos.append(nauja_knyga)
        self.issaugoti_knyga()

    def pasalinti(self, isleidimo_metai):
        self.knygos = [knyga for knyga in self.knygos if knyga.isleidimo_metai > isleidimo_metai]
        self.issaugoti_knyga()

    def ieskoti_knygos(self, ieskoti_pagal):
        return [knyga for knyga in self.knygos if ieskoti_pagal.lower() in knyga.pavadinimas.lower() or ieskoti_pagal.lower() in knyga.autorius.lower()]

    def knygu_sarasas(self):
        return self.knygos

    def neatnestu_knygu_sarasas(self):
        neatnestos_knygos = []
        for knyga in self.knygos:
            if knyga.ar_veluojama():
                neatnestos_knygos.append(knyga)
        return neatnestos_knygos