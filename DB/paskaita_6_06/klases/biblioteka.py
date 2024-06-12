
if __name__ == "__main__":
    from knyga import Knyga
else:
    from klases.knyga import Knyga
    
if __name__ == "__main__":
    from skaitytojas import Skaitytojas
else:
    from klases.skaitytojas import Skaitytojas

import sqlite3


class Biblioteka:
    def __init__(self, db_file = 'test7.db'):
        self.db_file = db_file
        self.knygos = []
        self.uzkrauti_knygas()
        self.sar_skaitytoju = []
        self.uzkrauti_skaitytojai()

    def uzkrauti_skaitytojai(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM User")
        rows = c.fetchall()
        self.sar_skaitytoju = [
            {'id': row[0], 'name': row[1]} for row in rows
        ]
        conn.close()
            
    def issaugoti_skaitytoja(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        for skaitytojas in self.sar_skaitytoju:
            c.execute(
                "INSERT INTO user (id, vardas) VALUES (?, ?, ?)",
                (skaitytojas['id'], skaitytojas['vardas'])
            )
        conn.commit()
        conn.close()    
            
            
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
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM Book")
        rows = c.fetchall()
        self.knygos = [
            {'id': row[0], 'pavadinimas': row[1], 'autorius': row[2], 'metai': row[3]} for row in rows
        ]
        conn.close()

    def issaugoti_knyga(self):
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()

            c.execute("DELETE FROM Book")

            c.execute(
                "INSERT INTO Book (name, author, year_made, type) VALUES (?, ?, ?, ?)",
                (name, author, year_made, type)
            )
            conn.commit()
            conn.close()


    def prideti_knyga(self, name, author, year_made, type):
        nauja_knyga = Knyga(name, author, year_made, type)
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