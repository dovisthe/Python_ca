class Animal:
    def __init__(self, akys, kojos):
        self.akys = akys
        self.kojos = kojos
        self.bega = True
        
    def begti(self):
        print(f'As turiu {self.akys} akis ir {self.kojos} kojas ir as begu')
        if self.bega is True:
            print("IR as begu greitai!")
        
        
class Kate(Animal):
    def __init__(self, akys, kojos, usai):
        super().__init__(akys, kojos)
        self.akys = akys
        self.kojos = kojos
        self.usau = usai
        
    def miauksi(self):
        print(f"Miau miau! Paziurek i mano {self.usau} usus")
        
        
class Suo(Animal):
    def __init__(self, akys, kojos, dantys):
        super().__init__(akys, kojos)
        self.akys = akys
        self.kojos = kojos
        self.dantys = dantys
        self.bega = False
        
    def loja(self):
        print(f"Au Au Au! Atsargiai man dantys yra {self.dantys}")
        

kate1 = Kate('dideles','keturios','ilgus baisiai')
kate2 = Kate('siauros','keturios','vidutiniai')

suo1 = Suo('sunio','dideles','astrus')
suo2 = Suo('sunio','dideles','buki')

counter = 0    
try:
    x = int(input("Ivesk kiek kartu gyvunai suksis : "))
    if x < 10:
        while counter < x:
            print('-' * 80)
            suo2.begti()
            suo1.loja()
            print('*' * 80)
            kate2.begti()
            kate1.miauksi()
            print('-' * 80)
            counter += 1
    else:
        print('ivesk skaiciu iki 10')    
except ValueError:
    print('ivesk skaiciu')