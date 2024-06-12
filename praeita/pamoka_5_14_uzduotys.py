import random
import pandas
import numpy

################################################
            #uzduotys
            #pirma uzduotis

# # sarasiukas
# sarasas = {"Darbininkai": ["justas", 'lukas', 'povilas']}

# #atspaudint
# print(sarasas['Darbininkai'])
# print(sarasas['Darbininkai'][0])
# print(sarasas)

# #prideti
# sarasas['Darbininkai'].append('Maikas')
# sarasas['Ofisas'] = ['DOvis', 'Jonas']
# print(sarasas)

# #istrinti
# del sarasas['Darbininkai']
# sarasas['Ofisas'] = ['Jonas']
# print(sarasas)

# #pakeisti
# sarasas['Ofisas'] = ["Cesiu", "Pyteris"]
# print(sarasas)


        #antra uzduotis


# skaiciai = []
# while True:
#     x = int(input('Ivestike norima skaiciu: '))
#     if x < 0:
#         break
#     skaiciai.append(x)

# print(skaiciai)

        #Trecia uzduotis
        

zodziu_sarasas = []

for i in range(5):
    zodis = input("iveskime zodi")
    zodziu_sarasas.append(zodis)
print("Ivesti zodziai")
print(zodziu_sarasas)
print(zodziu_sarasas.count)
