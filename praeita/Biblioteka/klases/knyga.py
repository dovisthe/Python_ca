from datetime import datetime 

class Knyga:
    def __init__(self, pavadinimas, autorius, isleidimo_metai, zanras):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isleidimo_metai = isleidimo_metai
        self.zanras = zanras
        self.kada_atiduoti = None
        self.ar_paimta = False

    def pasiskolinti(self, kada_atiduoti_data):
        self.kada_atiduoti = kada_atiduoti_data
        self.ar_paimta = True
        
    def grazinti(self):
        self.kada_atiduoti = None
        self.ar_paimta = False        

    def ar_veluojama(self):
        if self.kada_atiduoti is None:
            return False
        dabartine_data = datetime.now().date()
        return dabartine_data > self.kada_atiduoti
    
    
    
