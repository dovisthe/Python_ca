# def print_smth():
#     print("------------")
#     print("Hello world!")
#     print("Hello world!")
#     print("____________")
    
# def atspausdink(zodis):
#     print("------------")
#     print(zodis)
#     print("____________")
    
    
# #               5           3    
# def daugybas(skaicius1, skaicius2):
#     daugybos_res = skaicius1 * skaicius2
#     print(daugybos_res)    
    
# print_smth()
# print_smth()

# atspausdink("Rokas")
# atspausdink("Lukas")
# atspausdink("Maikas")

# daugybas(5, 3)
# daugybas(4, 7)
# daugybas(2, 3)
# ####################################
# def Mano_vardas(vardas):
#     print(vardas)
#     print("Hello you! \U0001F600")
    
# def dalyba(skaic1, skaic2):
#     dal_res = skaic1 / skaic2
#     print(dal_res)
    
# def sudetis(skc1, skc2):
#     sud = skc1 + skc2
#     print(sud)
    
# def grazus_oras():
#     print("Siandien yra grazus oras my g")
    
# def temp_keitiklis(temp):
#     f = (9/5 * temp) + 32
#     print("Fahreinheite temp butu: ")
#     print(f)
    
# Mano_vardas("dovis, eidikis")
# dalyba(15, 3)
# grazus_oras()
# sudetis(5, 5)
# temp_keitiklis(10)

# x = int(input("iveskite celsiu: "))

# temp_keitiklis(x)

# def daugybas(skaicius1, skaicius2):
#     daugybos_res = skaicius1 * skaicius2
#     return daugybos_res  #15

# res = daugybas(5, 3)  
# res2 = daugybas(res, 3)
# print(res2)
# print(res)

# def ar_lyginis(skaicius):
#     if skaicius % 2 == 0:
#         return "lyginis"
#     else:
#         return #None
    
# res = ar_lyginis(46545)

# print(res)

# if res:
#     print(res)
# else:
#     print("nieko nera")
    
# def count_letter(zodis):
#     print(zodis)
    
# count_letter('zodis')

# def daugybas(skc1, skc2):
#     sk = skc1 * skc2
#     print(sk)
    
# daugybas(1, 2)

# def ar_skc_didesnis_negu_10(sk):
#     if sk > 10:
#        return 'Lyginis'

        
# a = ar_skc_didesnis_negu_10(11)
# print(a)

# def ar_lyginis(skaicius):
#     return skaicius % 2 == 0


# def dienos(d1, d2, d3):
#     d_suma = 0
#     if ar_lyginis (d1):
#         d_suma += d1
#     if ar_lyginis (d2):
#         d_suma += d2
#     if ar_lyginis (d3):
#         d_suma += d3
#     return d_suma

# d_suma = dienos(4,5,6)
# print("otryju dienu lyginiu: ")
# print(d_suma)

# def kvadrato_plotas(krastine1, krastine2):
#     Plotas = krastine1 * krastine2
    
#     if Plotas > 10:
#         print(f' jusu krastiniu plotas yra: {Plotas}')
#         return Plotas
#     else:
#         print('plotas yra per mazas, irasykite didesnes krastines')
#         return 0
    
# kv_plotas = kvadrato_plotas(4, 4)
# if kv_plotas:
#     turis = kv_plotas * 3
#     print(f'turis bus{turis}')
    
    
# def nuotaika(balas):
#     if balas < 5:
#         return "blogai"
#     elif balas < 7:
#         return "viduriukas"
#     else:
#         return "gerai"
    
# x = int(input('Iveskite nuotaikos bala: '))
# ats = nuotaika(x)
# print(ats)



# def teksto_ilgis(tekstas):
#     return len(tekstas)

# x = input("Ivesk varda: ")
# vardo_ilgis = teksto_ilgis(x)
# print(vardo_ilgis)

# def atimtis(s1, s2):
#     sm = s1 - s2
#     return sm

# y = atimtis(10, 2)
# print(y)


# def skaiciai():
#     skaicius1 = float(input("Iveskite pirmaji skaiciu: "))
#     skaicius2 = float(input("Iveskite antraji skaiciu: "))
#     skaicius3 = float(input("Iveskite treciaji skaiciu:"))
#     suma = skaicius1 + skaicius2
#     rezultatas = suma * skaicius3
#     if rezultatas <= 0:
#         return f"Rezultatas neigiamas arba lygus nuliui{rezultatas}"
#     if rezultatas > 0:
#         return f"Rezultatas teigiamas{rezultatas}"
    

# print(skaiciai())



##################################################
# def zodzio_ilgis(zodis):
    
#     if len(zodis) > 10:
#         return 'zodis per ilgas '
#     else:
#         return f'{len(zodis)} - tinkamo ilgio'

# zodis1 = input('iveskite zodi')
# rezultatas = zodzio_ilgis(zodis1)
# print(rezultatas)

######################################################

# def sudetis(sk1 = 1, sk2 = 1 , sk3 = 1 ):
#     suma = sk1 + sk2 + sk3
#     return suma

# # rezultas = sudetis(2, 4, 6)
# # print(rezultas)

# # rezultas = sudetis()
# # print(rezultas)


# def sudetis_du_daugybas(sk1 = 1, sk2 = 1 , sk3 = 1 ):
#     suma = sk1 + sk2
#     suma = suma * sk3
#     return suma

# rezultas = sudetis_du_daugybas(1, sk3=2)
# print(rezultas)


# 5 skaiciu daugyba, bet 3 is ju yra optional
# 5 vardai ir visus juos sudeti i viena teksta, jie nera vardo, parasykim bevardis

# def daugyba_is_5(sk1, sk2, sk3=1, sk4=1, sk5=1):
#     suma = sk1 * sk2 * sk3 * sk4 * sk5
#     return suma


# ats = daugyba_is_5(1,2,3)
# print(ats)

# # 5 vardai ir visus juos sudeti i viena teksta, jie nera vardo, parasykim bevardis

# def vardu_jura(v1='bevardis', v2='bevardis', v3='bevardis', v4='bevardis', v5='bevardis'):
#     tekstas = (f'{v1} {v2} {v3} {v4} {v5}')
#     return tekstas.upper()

# x = input("Parasykite 5 zodzius su  kableliais: ")
# zodziai = x.split(",")

# rezultatas = vardu_jura(*zodziai)
# print(rezultatas)

# uppercase

# def vardas(tekstas, uppercase = False):
#     if uppercase:
#         tekstas = tekstas.upper()
#     else:
#         tekstas = tekstas.lower()
#     return tekstas

# naujas_tekstas = vardas('Dovydas Didikis yra mano vardas', True)
# print(naujas_tekstas)

#######################################################################################
# def atspausdink_visus(*args):
#     for item in args:
#         print(f'{item}')
        
# def suma(*args):
#     return sum(args)

# def maximum(*args):
#     return max(args)
                
        
# atspausdink_visus(3215,89,156,'tekstas',354,1314546,88,7)

# gauta_suma = suma(5,5,648,987)
# print('--------------')
# print(gauta_suma)

# gauta_max = maximum(5,5,648,987)
# print('--------------')
# print(gauta_max)
##################################################

# def atspausdink_visus_zodyno_duomenis(**kwargs):
#     for key, value in kwargs.items():
#         print(f'key: {key} - value: {value}')
        
# atspausdink_visus_zodyno_duomenis(vardas = 'Rokas', Profesija = 'programuotojas', Pomegis = 'futbolas', Amzius = 99)

#privalomieji parametrai
#*args
#nebutinieji parametrai
#**kwargs -- dictionary

# def my_func(a, b, *args, c = 5, d = 6, **kwargs):
#     print(a, b)
#     print(type(args), args)
#     print(c, d)
#     print(type(kwargs), kwargs)
    
# # my_func(2,9)
# my_func(1,1,2,2,2,c=3,d=3, skaicius = 4, tekstas = 'keturi', name = 'Rokas') 

# def args(*args):
#     print(type(args),args)
    
# args(1,2,3,'as',35,'kompiuteris')

# def kwargs(**kwargs):
#     print(type(kwargs), kwargs)
    
# kwargs(rusis = 'pythonas', lokacija = 'kaunas', situacija = 'tragiska')

# #-------------------------------------------------------------------------

# def atspausdink_visus(*args):
#     for item in args:
#         print(f'item : {item}')

# atspausdink_visus(55, 66, 'faktas seniuk')

# def listas(**kwargs):
#     for key, value in kwargs.items():
#         print(f'key: {key} - value:{value}')
        
# listas(rusis = 'pythonas', lokacija = 'kaunas', situacija = 'tragiska', finansu = 0)
#--------------------------------------------------------------------------------------------
# globalus = 10

# def func():
#     lokalus = 20
#     suma = lokalus + globalus
#     return suma

# nauja_suma = lokalus + globalus

# def maximum(*args):
#     '''
#     sita funkcija sudeda skaicius
#     :param : *args: yra sarasas skaiciu
#     :return: grazina maximuma
#     '''
#     return max(*args)


#----------------------------------

# def kvadratu(skaicius):
#     return skaicius ** 2

# #                 lambda [parametrai] : [veiksmai]
# #                 lambda x : x **2
# kvadratu_lambda = lambda skaicius : skaicius ** 2
# daugyba = lambda x, y : x * y

# sarasas = [5,2,8,2,5,5,9]

# resultatas_kvadratu = kvadratu_lambda(3)

# rez_kvadratu_sarasas = map(kvadratu_lambda, sarasas)

# for item in rez_kvadratu_sarasas:
#     print(item)



# # resultatas_daugyba = daugyba(4, 5)
# # print(resultatas_daugyba)


