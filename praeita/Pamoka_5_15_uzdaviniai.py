import datetime as dt

#     #Pirma uzduotis
    
# today = datetime.datetime.today()
# #atspausinti data ir laika
# x = datetime.datetime.now()
# print(x)

# #atimti 5 diena

# print(x - datetime.timedelta(days=5))

# #prideti 8 valandas

# print(x + datetime.timedelta(hours=8))

# # atspausdinti tokiu formatu 2019-03-08, 09:57:17

# print(x.strftime("%Y-%m-%d %H:%M:%S"))


    #antra uzduotis
    
ivesta_data = input("Iveskite data(MMMM-mm-dd): ")
data = dt.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
today = dt.datetime.now()

skirtumas = (today - data)
skirt = skirtumas.days

    #praejo metu:
print('Praejo metu')
print(round(skirt / 365))

# o = (today.year - data.year)
# print(o)

    #praejo menesiu
print('praejo menesiu')
x = (today.year - data.year) * 12 + (today.month - data.month)
print(x)

    #praeijo dienu
print('Praejo dienu')
print(skirt)

    #Praejo valandu
print('Praejo valandu')
z = skirtumas.total_seconds() / 3600
print(round(z))

    #Praejo minuciu
print('praeijo minuciu')
f = skirtumas.total_seconds() / 60
print(round(f))

    #Praejo sekundziu
print('praejo sekundziu')
print(round(skirtumas.total_seconds()))

