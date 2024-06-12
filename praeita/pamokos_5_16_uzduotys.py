import datetime as dt


# # Pirma uzduotis: grazina triju skaiciu suma---------------------------
# def sudetis(a,b,c):
#     sud = a+b+c
#     return sud
# x = sudetis(1,20,3)
# print(x)

# # #Antra uzd: grazintu paduoto saraso is skaiciu, suma--------------------
# def skaiciu_suma(sarasas):
#     return sum(sarasas)

# x = [1, 2, 3, 4, 5]

# suma = skaiciu_suma(x)
# print(f'saraso suma {suma}')

#trecia uzd:  atspausind did is keliu paduotu sk. (use *args)--------------

# def maximaliai(*args):
#     return max(args)

# x = maximaliai(20, 30, 50, 1)
# print(x)

# ketv uzd: grazintu paduota stringa atbulai -----------------------------

# def atbulai(zodis):
#     return zodis[::-1]

# x = atbulai('mechanikas')
# print(x)

#penkt uzd: atspausindti kiek paduotame stringe yra zodziu, didziuju ir mazuju raidziu skaiciu:

# def sakinukas(tekstas):
#     zodziu_skaiciu = len(tekstas.split())
#     did_raides = sum(1 for raide in tekstas if raide.isupper())
#     maz_raid = sum(1 for raide in tekstas if raide.islower())
#     return zodziu_skaiciu, did_raides, maz_raid


# x = "As einu Per pieva"
# zodziu, didziosios, mazosios = sakinukas(x)
# print("zodziu", zodziu)
# print("did skaicius", didziosios)
# print("maz skaicius", mazosios)

# sest uzd: grazinti sarasa tik su unikaliais paduoto saraso elementais--------------

# def sarasiukas(x):
#     naujas = list(set(x))
#     return naujas

# y = [1, 2, 3, 4, 4, 2, 5, 6, 6]
# z = sarasiukas(y)
# print(z)

# septinta uzd: grzintu ar paduotas skaicius yra pirminis--------------

# def pirminis(x):
#     if x > 1:
#         for i in range(2, (x//2)+1):
#             if (x % i) == 0:
#                 print(x, 'mera pirminis')
#                 break
#         else:
#             print(x, 'yra pirmins')
#     else:
#         print(x, 'mera pirminis')
  
# y = 12       
# z = pirminis(y)
# print(z)

# astunta uzd: isrikiuoti paduoto stringo zodzius nuo paskutinio iki pirmo------------

# def eilute_atbulai(x):
#     listas = x.split()
#     atvirksciai = ' '.join(listas[::-1])
#     return atvirksciai

# sakinys = "Mes esame pasaulyje apvaliame"
# x = eilute_atbulai(sakinys)
# print(x)

# devinta uzd: grazina ar duoti metai yra keliamieji ar ne--------------------------------

# lambda -----------
# ar_keliamieji = lambda metai: (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0)

# metai = 401
# if ar_keliamieji(metai):
#     print(f"{metai} yra keliamieji metai.")
# else:
#     print(f"{metai} nėra keliamieji metai.")
# #funkcija ----------
# def ar_keliami(metai):
#     if metai % 4 == 0 and metai % 100 != 0 or metai % 400 == 0:
#         return f'Yra keliamieji {metai}'
#     else:
#         return f'Nera keliamieji {metai}'

# x = 2000
# y = ar_keliami(x)
# print(y)


# desimta uzd: atspausdint, kiek nuo duotos datos praejo metu - sekundziu

def nuo_datos_praejo(norima_data):
    dabar = dt.datetime.now()
    x = dabar - norima_data
    return x
        
x_norimas = dt.datetime(1999, 10, 23, 15, 25, 10)
skirtumas = nuo_datos_praejo(x_norimas)
print("Nuo nurodytos datos praėjo:")
print("Metų:", skirtumas.days // 365)
print("Mėnesių:", (skirtumas.days % 365) // 30 * 12)
print("Dienų:", (skirtumas.days % 365) % 30)
print("Valandų:", skirtumas.seconds // 3600)
print("Minučių:", (skirtumas.seconds % 3600) // 60)
print("Sekundžių:", (skirtumas.seconds % 3600) % 60)

##################################################################---------------
# Antra skaidre
# pirma uzduotis: Patikrinti ar asmens kodas yra validus

# def ar_ak_valid(kodas):
#     kodo_skaicius= len(str(kodas))
#     if kodo_skaicius == 11:
#         return f'validus'
#     else:
#         return f'ne validus'

# ak = 39505090651
# x = ar_ak_valid(ak)
# print(x)

    
# def ar_tikras_ak(ak):
#     # paziurim ar 11 skaiciu ir ar isviso skaicius
#     if len(ak) != 11 or not ak.isdigit():
#         return False
    
#     # paziurim ar pirmas skaicius legit
#     pirm_skc = int(ak[0])
#     if pirm_skc not in range (1, 7):
#         return False
    
#     # tikrinkime gimimo data ar ji legit yra
#     simtmetis = (pirm_skc - 1) // 2 + 18
#     metai = simtmetis * 100 + int(ak[1:3])
#     menuo = int(ak[3:5])
#     diena = int(ak[5:7])
 
#     # tikrina ar atitinka data
#     def ar_data_legit(metai, menuo, diena):
#         try:
#             from datetime import datetime
#             datetime(metai, menuo, diena)
#             return True
#         except ValueError:
#             return False
                
#     if not ar_data_legit(metai, menuo, diena):
#         return False

#     return True

# # Test
# ak = '39505090635'
# if ar_tikras_ak(ak):
#     print(f"Asmens kodas {ak} yra teisingas.")
# else:
#     print(f"Asmens kodas {ak} yra neteisingas.")
    
# #antra uzduotis sukurti programa kuri pagal lyti metus ir eiles numeri


#trecia skaidre: 

def equal_halves(number):
    number_length = len(number)
    half_length = number_length // 2
    first_half = number[:half_length]
    second_half = number[half_length:]
 
    first_half_sum = sum(int(char) for char in first_half)
    second_half_sum = sum(int(char) for char in second_half)
 
    if first_half_sum == second_half_sum:
        return True
    else:
        return False
 
user_input = input("Enter your number: ")
print(equal_halves(user_input))
 
 
# 2
 
def adjacent_numbers(number):
    arr = []
    input_arr = list(number)  # Convert the input string to a list of characters
 
    for i in range(len(input_arr)):
        if int(input_arr[i]) == 0:  # Handle the first element case
            arr.append(f"{int(input_arr[i])} - 0{int(input_arr[i])+1}")
        elif int(input_arr[i]) == 9:  # Handle the last element case
            arr.append(f"{int(input_arr[i])} - {int(input_arr[i])-1}0")
        else:
            arr.append(f"{int(input_arr[i])} - {int(input_arr[i])-1}{int(input_arr[i])+1}")
    
    return arr
 
user_input = input("Enter your number: ")
print(adjacent_numbers(user_input))
