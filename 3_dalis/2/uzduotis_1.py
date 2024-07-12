import pandas as pd

labels = ['a','b','c','d','e']
sar = [1,2,3,4,5]

data = pd.Series(sar,labels)
print(data)
print("-------------------")
data = data.dtype
print(data)
print("-------------------")
data = pd.Series(sar)
print(data)
print("-------------------")
print(data[4])
print("-------------------")
print(data[1:4])
print("-------------------")
print(data[data>4])
print("-------------------")
print(data.sum())
print("-------------------")
print(data.mean())
print("-------------------")
data2 = data.apply(lambda x: x*2)
print(data2)
print("-------------------")


serija = [
    "Zodis",
    None,
    "Vardas",
    "Pavarde",
    "Amžius",
    None
]

x = pd.Series(serija)
print(x)

print("-------------------")

x1 = x.dropna()
print(x1)

print("-------------------")

x2 = x1.str.upper()
print(x2)

print("--------------------")

x3 = x2.value_counts()
print(x3)

print("--------------------")

x4 = x2.sort_values(ascending=True)
print(x4)

