import pandas as pd

import matplotlib.pyplot as plot

data = pd.read_csv("IMDb_Dataset.csv")

# print(data)

# print(data.head(10).to_string())
# print(data.describe())
print(data.columns)

data = data.drop_duplicates("Title")

films = data[["Title", "IMDb Rating", "Star Cast"]]

films = films[films["IMDb Rating"] > 8]

films = films.sort_values("IMDb Rating", ascending=False)

print(films['Title'].value_counts())

films.plot(kind="barh", title="FIlmu grafikas", x="Title", y="IMDb Rating")

plot.xlabel("Title")
plot.ylabel("IMDb Rating")
plot.show()

# print(films.isnull().sum())
print(films)