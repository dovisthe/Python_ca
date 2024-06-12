if __name__ == "__main__":
    import pajamuirasas as pi
else:
    from . import pajamuirasas as pi


if __name__ == "__main__":
    import isaliduirasas as isl
else:
    from . import isaliduirasas as isl


class Biudzetas:
    def __init__(self):
        self.zurnalas = []
        self.balansas = 0
   
    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
        irasas = pi.PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(irasas)
        self.balansas += suma
   
    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = isl.IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self.balansas -= suma
 
    def ataskaita(self):
        for irasas in self.zurnalas:    
            print(irasas)
        print(f'Balansas: {self.balansas}')
 
biudzetas = Biudzetas()