from datetime import datetime

# Pirma: Sukurti failą ir įrašyti Zen of Python
with open('Tekstas.txt', 'w', encoding='utf-8') as file:
    x = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
    file.write(x)

# Antra: Perskaityti failą
with open('Tekstas.txt', 'r', encoding='utf-8') as file:
    print(file.read())

# Trečia: Pridėti laiko žymę
with open('Tekstas.txt', 'a', encoding='utf-8') as file:
    file.write(datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '\n')

# Ketvirta: Numeruoti eilutes
# with open("Tekstas.txt", "r", encoding='utf-8') as file:
#     lines = file.readlines()

# with open("Tekstas.txt", "w", encoding='utf-8') as file:
#     for i, line in enumerate(lines, 1):  # Pradedame nuo 1
#         file.write(f"{i}. {line}")

# Penkta: Pakeisti eilutę "Beautiful is better than ugly."
with open('Tekstas.txt', 'r', encoding='utf-8') as file:
    lines2 = file.readlines()

lines2 = [line if "Beautiful is better than ugly." not in line else "Gražu yra geriau nei bjauru\n" for line in lines2]

#Ketvirta
with open("Tekstas.txt", "w", encoding='utf-8') as file:
    for i, line in enumerate(lines2, 1):  # Pradedame nuo 1
        file.write(f"{i}. {line}")

with open('Tekstas.txt', 'r', encoding='utf-8') as file:
    print(file.read())

# Šešta: Atspausdinti atbulai
with open('Tekstas.txt', 'r', encoding='utf-8') as file:
    lines3 = file.read()
    atvirksciai = lines3[::-1]
    print(atvirksciai)

# Septinta: atspausdinti, kiek tekste yra zodziu, skaiciu, did ir maz raidziu

with open('Tekstas.txt', 'r', encoding='utf-8') as file:
    lines4 = file.read()
    zodziai = lines4.split()
    zodziu_skaicius = len(zodziai)
    print(f'Zodziu skaicius: {zodziu_skaicius}')
    
    skaiciai = 0
    for sk in lines4:
        if sk.isdigit():
            skaiciai += 1
    print(f'SKaiciu kiekis: {skaiciai}')
    skc1 = 0
    for did in lines4:
        if did.isupper():
            skc1 += 1
    print(f'Didziuju skaicius: {skc1}')
    skc2 = 0
    for maz in lines4:
        if maz.islower():
            skc2 += 1
    print(f'MAzuju skaicius: {skc2}')
    
# septinta nukopint visa sukurta txt i nauja faila su did raidem

with open('Tekstas.txt', 'rb') as r_file:
    with open("Teksto_kopija.txt", 'wb') as w_file:
        for r_eilute in r_file:
            x = r_eilute.upper()
            w_file.write(x)
    
    

    