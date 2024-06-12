# pinigai = 20
 
# if pinigai >= 500 and pinigai < 1500:
#     print("Dar pinigu pakanka")
# elif pinigai > 1500 and pinigai < 5000:
#     print("Turi daug pinigu")
# elif pinigai > 5000:
#     print("Tu esi turtingas")
# else:
#     print("Tu esi vargsas")

########################################################
    
# skaicius = 5
# skaicius1 = 8
# skaicius2 = 15

# skaiciai = [skaicius,skaicius1,skaicius2,20]

# print(skaiciai.index(15))
# print(skaiciai)

# print(skaiciai[2])
# skaiciai.append(101)

# skaiciai.remove(8) # vieta istrina grynai pagal paty skaiciu lenteleje
# skaiciai.pop(2)  #vieta istrini su indexu

# print(skaiciai)

# skaiciai[0] = 1
# print(skaiciai)
#################
# skaicius = 5
# skaicius1 = 8
# skaicius2 = 15
 
# skaiciai = [skaicius,skaicius1,skaicius2,20]
 
# print(skaiciai)
 
# print(skaiciai[2])
# skaiciai.append(101)
 
# skaiciai.pop(3)
 
# skaiciai[0] = 1
# print(skaiciai)

#####################################################################

# amziai = {"Arnas":[5,7,9], "Vaidas":15, "Karolina":25}

# print(amziai["Arnas"])

# greiciai = {1:7,2:7.15,3:8}

# print(greiciai[1])

# greiciai[4] = 8.20

# greiciai[1] = 6.58

# del greiciai[4]

# print(greiciai)

######################################################################


# for skaicius in range(10):
#     print(skaicius)
    
# suma = 0    
# kiekis = int(input("iveskite kieki "))
# for skaicius in range(kiekis):
#     suma = suma + skaicius
    
# print(suma)
######################################
# suma = 0    
# kiekis = int(input("iveskite kieki "))
# for skaicius in range(kiekis):
#     print(skaicius)
#     if (skaicius % 2) == 0: # jei gale lieka nulis, tia lyginis skaicius
#         suma += skaicius
# print(suma)

# suma = 0    
# skaiciai = [5,7,9,1,5,4]

# for skaicius in skaiciai:
#     print(skaicius)
#     if (skaicius % 2) == 0: # jei gale lieka nulis, tia lyginis skaicius
#         suma += skaicius
# print(suma)

# amziai = {"Arnas":[5,7,9], "Vaidas":15, "Karolina":25}

# # values : keys
# for vardas, amzius in amziai.items():
#     print(vardas)

#############################
# Kiekis = 0
# while 10 > Kiekis:
#     print("Labas")
#     Kiekis = Kiekis + 1
    
###################

# Kiekis = 0
# while 10 > Kiekis:
#     print("Labas")
#     if input("Ivesk kazka ") == '':
#         break

###########################


# kiekis = 0
# kiekis_vid = 0

# while kiekis < 10:
#     print("Isorinio ciklo kiekis: ", kiekis)
#     while kiekis_vid < 5:
#         print(f"Vidinio ciklo kiekis: {kiekis_vid}")
#         kiekis_vid += 1
#         if kiekis_vid == 3:
#            break
#     kiekis + kiekis +1
#     kiekis_vid = 0
    
# while kiekis < len(skaiciai):
#     print(skaiciai[kiekis])
#     kiekis += 1


# my_list = [1, 2, 3]
# print(4 in my_list)
# my_tuple = (1, 2, 3)
# print(my_list[0])

# kiekis = 0
# suma = 0
# while kiekis < 10000:
#     print(kiekis)
#     kiekis += 1
# print(suma)

# if 5 > 1:
#     pass
# print("hi")    #nenaudoti


# user = "Johnny"
# privileged_users = ["Tom", "Albert", "Stephen"]
# if user in privileged_users:
#     print(f"Welcome home {user}")
# else:
#     print("INTRUDER ALLERT. Silently calling police...")

# my_list = []
# if not my_list:
#   print("oh no, list is empty")

# dict_one = {'a': 10, 'b': 20, 'c': 30}
# dict_two = {'b': 200, 'd': 400}
# dict_one .update(dict_two )
# print(dict_one )


# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)