import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Python_ca\\3_dalis\\3\\train.csv')
print(df)

# df.fillna(10, inplace=True)

print("-----------------------------")

# x = pd.DataFrame(df, columns=["SibSp", "Parch"])
# print(x)
# siblings = df["SibSp"].sum()
# parents = df["Parch"].sum()
#?
# df["Familiskaiciuotuvas"] = df["SibSp"] + df["Parch"]
# print(df)
#?
# print(f"siblings: {siblings}, parents: {parents}")

print("-----------------------------")

# def pagal_amzius(metai):
#     if metai <= 18:
#         return "Maziausias"
#     elif metai <= 65:
#         return "Vidutinis"
#     else:
#         return "Didelis"
    
# df["kas mazdaug"] = df["Age"].apply(pagal_amzius)
# print(df)

print("-----------------------------")

# df['Alone'] = ((df['SibSp'] + df['Parch']) == 0).astype(int)

# df['Surname'] = df['Name'].apply(lambda name: name.split(',')[0])

# surname_counts = df['Surname'].value_counts()

# df['FamilySize'] = df['Surname'].map(surname_counts)

# df['HasFamily'] = (df['FamilySize'] > 1).astype(int)
# print(df[['Name', 'SibSp', 'Parch', 'Alone', 'Surname', 'FamilySize', 'HasFamily']])
# print(df)

# print("-----------------------------")

# x = df.groupby("Pclass")["Age"].mean()

# print(x)

# print("---------------------------------")

# y = df.groupby("Pclass")['Survived'].mean()

# print(y)

# print("---------------------------------")

# sex = df.groupby('Sex')['Survived'].mean()

# print(sex)

# print("---------------------------------")

q = df.groupby("Embarked")['Survived'].mean()

print(q)


import seaborn as sns

# sns.catplot(x='Pclass', y='Survived', hue='Sex', data=df, kind='point')
# plt.show()

# sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm')
# plt.title('Heatmap')
# plt.show()


# x = pd.get_dummies(df, columns=['Name'])
# print(x)