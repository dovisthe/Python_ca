import datetime as dt

# class Sukaktis:
#     def __init__(self, metai, menuo, diena, valanda, minute, sekunde):
#         self.data = dt.datetime(metai, menuo, diena, valanda, minute, sekunde)
        
#     def praejo_metu(self):
#         dabar = dt.datetime.now()
#         skirtumas = dabar - self.data
#         metai = skirtumas.days // 365
#         likusios_dienos = skirtumas.days % 365
#         menesiai = likusios_dienos // 30
#         dienos = likusios_dienos % 30
#         valandos = skirtumas.seconds // 3600
#         minutes = (skirtumas.seconds % 3600) // 60
#         sekundes = skirtumas.seconds % 60
        
#         print("Nuo nurodytos datos praėjo:")
#         print(f"Metų: {metai}")
#         print(f"Mėnesių: {menesiai}")
#         print(f"Dienų: {dienos}")
#         print(f"Valandų: {valandos}")
#         print(f"Minučių: {minutes}")
#         print(f"Sekundžių: {sekundes}")

#     def ar_keliamieji(self):
#         dabar = dt.datetime.now()
#         skirtumas = dabar - self.data
#         metai = skirtumas.days // 365
#         if metai % 4 == 0 and metai % 100 != 0 or metai % 400 == 0:
#             print(f'Yra keliamieji {metai}')
#         else:
#             print(f'Nera keliamieji {metai}')              

#     def atima_5_dienas(self):
#         atimama_penkias = self.data - dt.timedelta(days=5)
#         print(atimama_penkias)
        
#     def pridedam_5_dienas(self):
#         prideda_penkias = self.data + dt.timedelta(days=5)
#         print(prideda_penkias)
        


# data1 = Sukaktis(1999, 10, 23, 15, 25, 10)


# data1.praejo_metu()
# data1.ar_keliamieji()
# data1.atima_5_dienas()
# data1.pridedam_5_dienas()

#Trecia skaidriu uzduotis ==--------------------------------------------------------------------------------


# class Default:
#     def __init__(self, nieko=12):
#         self.default = nieko

#     def atspausdinam_kazka(self):
#         x = self.default
#         print(x)
        
# data = Default()

# data.atspausdinam_kazka()
        
# class Gimtadienis:
#     def __init__(self, metai=1995, menuo=5, diena=9):
#         self.data = dt.datetime(metai, menuo, diena)
    
#     def kiek_praejo_nuo_gim(self):
#         dabar = dt.datetime.now()
#         praejo = dabar - self.data
#         print(praejo)
        
#     def __str__(self):
#         return self.data    
        
        
# data_kokia_gimimo = Gimtadienis()

# data_kokia_gimimo.kiek_praejo_nuo_gim()

#KEtvirta skaidre-----------------------------------------

class Sakin:
    def __init__(self, zodis='Taip'):
        self.tekstas = zodis
        
    def ar(self):
        txt = self.tekstas
        print(txt)
        
    def __str__(self):
        return self.tekstas
    
x = Sakin()

x.ar()
print(x)


class Data:
    def __init__(self, metai=1995, menuo=5, diena=9):
        self.data = dt.datetime(metai, menuo, diena)
        
    def data_gim(self):
        gim = self.data
        print(gim)
            
    def __str__(self):
        return self.data.strftime("%Y-%m-%d")
    
y = Data(2015, 5, 5)
z = Data()

y.data_gim()

print(z)