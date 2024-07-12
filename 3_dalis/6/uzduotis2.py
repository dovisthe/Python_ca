from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv('C:\\Python_ca\\3_dalis\\6\\train.csv')

#Train.csv ------------------------------------

df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF'] + df['GarageArea']
df['AgeOfHouse'] = df['YrSold'] - df['YearBuilt']

categorical_cols = df.select_dtypes(include=['object', 'category']).columns

for column in categorical_cols:
    missing = df[column].isna().sum()
    percent_missing = (missing / len(df)) * 100
    if 40 >= percent_missing:
        df[column] = df[column].fillna(df[column].mode()[0])
    else:
        df = df.drop([column], axis=1)

df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())
df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].mean())
df['GarageYrBlt'] = df['GarageYrBlt'].fillna(df['GarageYrBlt'].mean())

label_encoder = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

for column in categorical_cols:
    df = pd.get_dummies(df, columns=[column], drop_first=True)
 
numeric_cols = df.select_dtypes(include=['int', 'float']).columns
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols]) 
 
Q1 = df['LotArea'].quantile(0.25)
Q3 = df['LotArea'].quantile(0.75)
IQR = Q3 - Q1  
upperFilter = (df['LotArea'] >= Q3 + 1.5 *IQR)
lowerFilter = (df['LotArea'] <= Q1 - 1.5 *IQR)
df.loc[upperFilter,['LotArea']]  = Q3 + 1.5 *IQR
df.loc[lowerFilter,['LotArea']]  = Q1 - 1.5 *IQR


plt.figure(figsize=(10, 6))
plt.hist(df['LotArea'], bins=30, edgecolor='black')
plt.title('Histogram of LotArea')
plt.xlabel('LotArea')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


import numpy as np
X = df[numeric_cols]

X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 6))
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.5, align='center')
plt.step(range(1, len(pca.explained_variance_ratio_) + 1), np.cumsum(pca.explained_variance_ratio_), where='mid')
plt.title('Explained Variance by Principal Components')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.grid(True)
plt.show()
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)
n_components = np.argmax(cumulative_variance_ratio >= 0.95) + 1
print(f'Number of components to retain: {n_components}')


pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)


# X = df.drop(columns=['SalePrice'])
# y = df['SalePrice']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# k = 5
# knn = KNeighborsClassifier(n_neighbors=k)
# knn.fit(X_train, y_train)

# y_pred = knn.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')