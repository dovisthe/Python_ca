class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma
   
    def __str__(self):
        return f"suma: {self.suma}, tipas: {self.tipas} "
   
 
class Biudzetas:
    def __init__(self):
        self.zurnalas = []
        self.balansas = 0
   
    def prideti_pajamu_irasa(self, suma):
        irasas = Irasas("Pajamos", suma)
        self.zurnalas.append(irasas)
        self.balansas += suma
   
    def prideti_islaidu_irasa(self, suma):
        irasas = Irasas("Islaidos", suma)
        self.zurnalas.append(irasas)
        self.balansas -= suma
 
biudzetas = Biudzetas()
 
while True:
    pasirinkimas = input("Pasirinkite veiksma:\n1. Prideti pajamas\n2. Prideti islaidas\n3. Parodyti balansa\n4. Baigti\n")
   
    if pasirinkimas == "1":
        pajamos = int(input("Iveskite pajamas: "))
        biudzetas.prideti_pajamu_irasa(pajamos)
   
    elif pasirinkimas == "2":
        islaidos = int(input("Iveskite islaidas: "))
        biudzetas.prideti_islaidu_irasa(islaidos)
 
    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.balansas}")
 
    elif pasirinkimas == "4":
        print("Programa baige darba.")
        break
 
    else:
        print("Netinkamas pasirinkimas. Bandykite dar karta.")