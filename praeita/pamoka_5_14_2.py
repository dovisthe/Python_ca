import pandas
import numpy

# pirma uzduotis
# skaicius1 = int(input('Iveskite skaiciu: '))
# skaicius2 = int(input('Iveskite skaiciu: '))

# if skaicius1 < skaicius2:
#     print('pirmas skaicius yra mazesnis uz antra')
# elif skaicius1 == skaicius2:
#     print('lygu')
# else:
#     print('antras mazesnis')

#antra uzduotis

# zodis = 'Zen of Python'

# print(zodis[5:6])
# print(zodis[7:8])
# print(zodis[0:3])
# print(zodis[7:13])
# print(zodis[::-1])
# print(zodis.split())
# print(zodis.replace('Python', 'Programuotojas'))
# atskiras = zodis.split()
# print(atskiras[0][-1])

# trecia uzduotis

# zodis = 'belgas'
# print(zodis.upper())
# zodis2 = 'Do ThE wOrK BlA bla BLa'
# print(zodis2.casefold())
# print(zodis.capitalize())
# print(zodis2.count('B'))
# print(zodis2.find('w'))

# ketvirta

# x = float(input('iveskite pirma skaiciu :'))
# z = float(input('iveskite antra skaiciu :'))

# skaiciavimas = input('Koki matematini veiksma norite atlikti? (+, -, *, /): ')


# if skaiciavimas == '+':
#     rezultatas = x + z
#     print(rezultatas)
# elif skaiciavimas == '-':
#     rezultatas = x - z
#     print(rezultatas)
# elif skaiciavimas == '*':
#     rezultatas = x * z
#     print(rezultatas)
# elif skaiciavimas == '/':
#     rezultatas = x / z
#     print(rezultatas)
# else:
#     print('Neteisingai ivestas skaiciavimo metodas')

#**************************************************************************
# penkta
#?????????????????????????????????????????????????????????????????????????????????????
# input:

# Enter email addresses separated by commas: john.doe@example.com,
# jane.smith@anotherexample.com, max.power@coolmail.com

# output:

# Formatted Names:
# John Doe
# Jane Smith
# Max Power


# email = input('Iveskite emaila kuri skiria taskai? :')

# atskiri = email.replace(',', ' ')

# nuimame_Eta = atskiri.split('@')[0].replace('.', ' ')
# print('Vardas ir pavarde: ')
# print(nuimame_Eta.split(' ')[0].capitalize(), nuimame_Eta.split(' ')[1].capitalize())
# nuimame_Eta = atskiri.split('@')[0].replace('.', ' ')
# print(nuimame_Eta.split(' ')[1].capitalize(), nuimame_Eta.split(' ')[1].capitalize())

#????????????????????????????????????????????????????????????????????????????????????????


            #13:00

# zodziai = "Labas kaip tau sekasi? 5".split()
# # zodziai = ["Labas", "Kaip", "Sekasi", "Siandie"]

# print(zodziai)

# skaiciai = [2, 3, 5, 9, 100, 7, 15, -5]


# print(skaiciai[0])
# print(zodziai[3])

# skaic_sakic = [[5,7,9],[5,6,1]]
# print(skaic_sakic[0][0])

# saikciai = [5,7,9]

# print(saikciai)

# saikciai.append(15)
# print(saikciai)
# print(saikciai[-1])

# saikciai = [5,7,9]

# saikciai.append(15)
# print(saikciai)

# saikciai[0] = 8
# print(saikciai)
# # saikciai.pop(0)
# # print(saikciai)


# print(len(saikciai))

# pazymiai = {"Justas" : [7,5,9], 2: [1,4,9], "Karolis": [9,5,9]}
# print(pazymiai)

# print(pazymiai['Justas'])
# print(pazymiai[2])

# skaiciai = [5,7,9,5]
# skaiciai = {0:5,1:7,2:9,3:5}

# kompanijos = {"CodeAcademy":["Justas","Paulius","Edvinas"],
#               "Maxima":["Petras","Arturas"]}

# kompanijos["Norfa"] = ["Laura","Tomas"]

# del kompanijos["Maxima"]
# print(kompanijos)

# darbuotojai = kompanijos["Norfa"]
# darbuotojai.append('Karolis')
# print(darbuotojai)
# kompanijos["Norfa"] = darbuotojai
# print(kompanijos)

# kompanijos["Norfa"].append("Karolis")
# print(kompanijos)

# skaiciai = [5,7,9,5]

# suma = 0

# for skaicius in skaiciai:
#     suma += skaicius
#     print('dabartine sume: ', suma)
# print('galutine suma', suma/len(skaiciai))

# kompanijos = {"CodeAcademy":["Justas","Paulius","Edvinas"],
#               "Maxima":["Petras","Arturas"]}

# kompanijos["Norfa"] = ["Laura","Tomas"]

# for raktas, reiksme in kompanijos.items():
#     print(f"{raktas} darbuotoja yra: {reiksme}")
############################################################

# for skaicius in range(2, 15, 3):
#     print(skaicius)
##################################################

# limitas = 100
# i = 1
# while i < limitas:
#     print(i) 
#     i += 1

###############################
    
    
    
# for skaicius in range(10):
#     print(skaicius)
#     if (int(input("ivesk skaiciu")) >= 7):
#         break
    
#################################

# for skaicius in range(10):
#     if (skaicius >= 7):
#         continue
#     print(skaicius)

#####################################

# for skaicius in range(10):
#     print(skaicius)
# else:
#     print("pabaiga")

# random_integer = random.randint(1, 10)
# print(random_integer)

################################################
            #uzduotys
            #pirma uzduotis

# suma = 0
 
# for skaicius in skaiciai:
#     suma += skaicius
#     print("Dabartine suma: ", suma)
# print("Galutinis vidurkis",suma/len(skaiciai))
 
# for raktas, reiksme in kompanijos.items():
#     print(f"{raktas} darbuotojai yra: {reiksme}")
 
# for skaicius in range(50):
#     print(skaicius)
 
# limitas = 100
# i = 1
# while i < limitas:
#     print(i)
#     i +=1
 
# Input 15....
 
# for skaicius in range(10):
#     print("Pirmas spausdinimas", skaicius)
#     if(skaicius >= 3):
#         continue
#     print(skaicius)
 
 
# for skaicius in range(10):
#     print(skaicius)
# else:
#     print("Pabaiga")