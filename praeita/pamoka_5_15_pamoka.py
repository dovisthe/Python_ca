import datetime


# skaicius = int(input("Iveskite skaiciu :"))

# ar_skaicius_teigiamas = bool() #NEBUTINAS
# if skaicius > 0:
#     ar_skaicius_teigiamas = True
# else:
#     ar_skaicius_teigiamas = False
    
# print(ar_skaicius_teigiamas)
########################################################
# x = datetime.datetime.today()
# print(x)

# siandien = datetime.datetime.today()
# print(siandien)

# print(datetime.date.today())

# print(datetime.datetime.today().time()

# data = datetime.datetime(2022,10,15,10,15,11)

# print(data)

# print(data.strftime("%d %y")) #%H {}

# print(datetime.date.today().strftime("%j"))

# data = datetime.datetime(2022,10,15,10,15,11)

# print(data - datetime.timedelta(days=30))

# print(data + datetime.timedelta(hours=30))
# print(data + datetime.timedelta(hours=30, days=3))


# # ieskome kad ivestu tinkama formata, antaipp error
# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# today = datetime.datetime.today()
# # print('Jusu gimimo data yra: ', gimimo_data)

# skirtumas = (datetime.datetime.now() - gimimo_data)
# print(skirtumas.days)
# print('Jums yra :',skirtumas.days / 365)

# age = today.year - gimimo_data.year - ((today))

# print((today.month, today.day))
# print((gimimo_data.month))

# try:
#     # 7 / 0
#     # int("Hello")
#     "labas" - 5
#     open("Neegzistuojantis.txt")
#     print(7/1)
# except ZeroDivisionError:
#     print("Dalyba is nulio negalima")
#     print()
#     print()
#     print()
#     print()
#     print()
# except ValueError:
#     print("Pateikta netinkama reiksme")
# except TypeError:
#     print("Neteisingas tipas")
# except:
#     print("Nenumatyta klaida")
 
# print("Labas")

while True:
    try:
        x = int(input('Iveskite skaiciu: '))
        break
    except:
        print('Bandyk is naujo G')
print(f'good job NO CAP you number is {x} my G')


try:
    # 7 / 0
    # int("Hello")
    # "labas" - 5
    try:
        open("Neegzistuojantis.txt")
    except:
        print("vidine klaida")
   
    print(7/1)
except ZeroDivisionError:
    print("Dalyba is nulio negalima")
    print()
except ValueError:
    print("Pateikta netinkama reiksme")
except TypeError:
    print("Neteisingas tipas")
except Exception as e:
    print(e)
finally:
    print("Nesvarbu pavyko ar nepavyko as cia") #isjunk programa
 
 
print("Labas")

