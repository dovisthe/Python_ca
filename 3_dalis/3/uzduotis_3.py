import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = {"humidity": np.random.uniform(low=10, high=30.0, size=5)}
data = {"Miestas": ['Kaunas', 'Vilnius', 'Klaipeda', 'Siauliai', 'Visaginas'],
        "Oro kokybe": ["Gera", "Bloga", "Bloga" ,"Bloga" ,"Bloga"],
        "Temp": [10,-5,15,13,0]
}

df = pd.DataFrame(data)

print(df)

print("-------------------------------")

print(df.iloc[1])
print(df.iloc[4])

print("-------------------------------")

print(df["Temp"].mean())

print("-------------------------------")

print(df[df["Temp"]<0])

print("-------------------------------")

df["vejas"] = np.random.randint(low=1, high=50, size=5) # pagal valdemara
print(df)

print("----------------------------------")

df["Persalimo rizika"] = df["Temp"].apply(lambda x: "Taip" if x < 0 else "Ne")

print(df)

print("--------------------------------")

def vejo_stipr(vejas):
    if vejas < 10:
        return 'silpnas'
    elif vejas <= 20:
        return 'vidutinis'
    else:
        return 'super'

df["vejas"] = df["vejas"].apply(vejo_stipr)
print(df)

print("-----------------------------------")

x = df.groupby("Persalimo rizika")["Temp"].mean()
print(x)

print("----------------------------------")

print(df.sort_values(by = "Temp", ascending=False))

print("---------------------------------")

data2 ={"Miestas": ['Kaunas', 'Vilnius', 'Klaipeda', 'Siauliai', 'Visaginas'],
        "Ar miesats bangeris?": ["Taip", "NE","NE","NE","NE"]
}

df2 = pd.DataFrame(data2)

y = pd.merge(df, df2, on="Miestas", how="inner")
print(y)
