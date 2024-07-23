import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

#Užduotis: Sukurkite 3D NumPy masyvą su (2, 3, 4) forma,
# užpildytą atsitiktiniais skaičiais.--------------------------------------------

# data = np.random.randint(2,10, (2,3,4))

# print(data)

# scaler = MinMaxScaler()
# scaled_data = scaler.fit_transform(data)

# print(scaled_data)

#Užduotis: Sukurkite 2D masyvą su 5x5 dimensijomis, 
# užpildytą atsitiktiniais sveikaisiais skaičiais tarp 0 ir 100.----------------------------

# data2 = np.random.randint(0,100, (5,5))
# print(data2)

# print(f"Shape: {data2.shape}")
# print(f"Data type: {data2.dtype}")

# column_mean = np.mean(data2, axis=0)
# column_std = np.std(data2, axis=0)

# print(column_mean)
# print(column_std)


# data2_normalized = (data2 - column_mean) / column_std
# print(data2_normalized)

# data2_squared = np.square(data2)
# print(data2_squared)

# #Sukurkite Pandas DataFrame su 4 stulpeliais------------------------------------
# # ('Produktas', 'Kaina', 'Kiekis', 'Kategorija') ir 10 atsitiktinių duomenų eilutėmis.


produktai = np.random.randint(1, 20, size=10)
kainos = np.random.randint(1, 100, size=10)
kiekiai = np.random.randint(1, 1000, size=10)
kategorijos = np.random.randint(1, 6, size=10)  


data3 = pd.DataFrame({
    'Produktas': produktai,
    'Kaina': kainos,
    'Kiekis': kiekiai,
    'Kategorija': kategorijos
})

df = pd.DataFrame(data3)
print(df)


df["Bendras kiekis"] = df["Kaina"] * df["Kiekis"]

print(df)

#randam kur kategorija yra 1
x1 = df['Kategorija'].apply(lambda x: 1 == x)

print(x1)

#Vidutine kaina pagal kategorija
x2 = df.groupby("Kategorija")['Kaina'].mean()

print(x2)
# pivot lentele, bendras kainu kiekis kategorijos
pivot_table = df.pivot_table(values='Kaina', index='Kategorija', aggfunc='mean')

print(pivot_table)