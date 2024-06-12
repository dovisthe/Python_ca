import os

current_directory = os.getcwd()
print('Dabartinis katalogas:', current_directory)

# items = os.listdir(current_directory)
# print('Katalogo turinys', items)

# os.mkdir('Naujas') # pakuria folder
# os.rmdir("Naujas") # pasalina folder

# os.makedirs("Naujas/Jonas/Tomas")
# os.removedirs("Naujas/Jonas/Tomas")

# with open('naujas_failas.txt', 'w') as file:
#     for skaicius in range(1, 100):
#         file.write(f'{skaicius}: naujas failas, labas\n')

# with open('naujas_failas.txt', 'a') as file:
#     for skaicius in range(1, 100):
#         file.write(f'{skaicius}: pridedamas textas\n')

# with open('naujas_failas.txt', 'r') as file:
#     for eilute in file:
#         print(eilute)

# with open('naujas_failas.txt', 'r') as file:
#     print(file.readline())
#     print(file.readlines())


# os.rename('naujas_failas.txt', 'PVZ_failas.txt')

# os.remove('PVZ_failas.txt')

# items = os.listdir(current_directory)

# for item in items:
#     if os.path.isfile(item):
#         print(f'Failas: {item} ')
#     else:
#         print(f'Aplankas: {item} ')

items = os.listdir(current_directory)

for item in items:
    if os.path.isfile(item):
        print(f'Failas: {item} ')
    elif os.path.isdir(item):
        print(f'Aplankas: {item} ')