from statistics import mean, median


# Pirma skaidre----------------------------------------

# x = """The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated."""

# sakiniai = x.split('\n')
# pakeisti_sakiniai = list(map(lambda sakinys: sakinys + '!', sakiniai))
# su_sauktukais = '\n'.join(pakeisti_sakiniai)
# print(su_sauktukais)

# Antra skaidre ------------------------------------------

# #Pirm sukurt sarasa 0 - 50

# x = list(map(lambda i: i, range(0, 51)))
# print(x)

# #antra padaugint viska is 10

# y = list(map(lambda skaicius: skaicius * 10, x))
# print(y)

# #trecia atrinktu kurie dalinasi is 7

# dalinasi = list(filter(lambda dal: dal % 7 ==0, x))
# print(dalinasi)

# #Ketvirta pakelti visus kvadratu

# kvdrt = list(map(lambda kv: kv ** 2, x))
# print(kvdrt)

# # penkta atspausdint: suma, maziausia, didz, vidur , median

# suma = sum(kvdrt)
# print(f'SUma yra: {suma}')
# maziaus = min(kvdrt)
# print(f'maziausias skaicius {maziaus}')
# didz = max(kvdrt)
# print(f'didziausias skaicius {didz}')
# vidurkis = mean(kvdrt)
# print(f'Vidurkis yra: {vidurkis:>{1}.0f}')
# mediana = median(kvdrt)
# print(f'Mediana yra: {mediana}')

# atbulai = kvdrt.sort(reverse=True)
# # atbulai = sorted(kvdrt, reverse=True)
# print(atbulai)

# Trecia skaidre: ---------------------------------------------------------

# pirma uzduotis
# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# # skaiciu suma
# # skaiciai = list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), sarasas))
# # y = sum(skaiciai)
# # print(f'Skaiciu suma {y}')

# skaiciai = [s for s in sarasas if type(s) == float or type(s) == int]
# y = sum(skaiciai)
# print(f'Skaiciu suma {y}')

# print(sum(list(type(c) is int or type(c) is float for c in sarasas)))

#antra uzduotis

# zodziai = list(filter(lambda x: isinstance(x, str), sarasas))
# x = " ".join(zodziai)
# print(f'Zodziu sarasas: {x}')

# #Trecia uz

# loginiai = list(filter(lambda x: isinstance(x, bool), sarasas))
# kiek_True = loginiai.count(True)
# print(kiek_True)

# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# print(sum(list(type(c) is int or type(c) is float for c in sarasas)))


# print(list(type(c) is str for c in sarasas))

#Ketvirta skaidre ------------------------------------------------------------------------

# Pirma uzduotis

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
        
    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")
    
zmg1 = Zmogus('Maikas', 15)
zmg2 = Zmogus("Pyteris", 55)
zmg3 = Zmogus("Zimeris", 13)
zmg4 = Zmogus("Praisas", 5)

sarasas = [zmg1, zmg2, zmg3, zmg4]

def rusiavimas(zmogus):
    return zmogus.vardas

surusiuotas = sorted(sarasas, key=rusiavimas)
print(f'Pagal vardus: {surusiuotas}')
surusiuotas.reverse()
print(f'Atbulai: {surusiuotas}')

# surusiuotas = sorted(sarasas, key=lambda e: e.amzius)
# print(f'Pagal amziu: {surusiuotas}')

from operator import attrgetter

surusiuotas = sorted(sarasas, key=attrgetter("amzius"))
print(f'Pagal amziu: {surusiuotas}')
surusiuotas.reverse()
print(f'Atbulai: {surusiuotas}')