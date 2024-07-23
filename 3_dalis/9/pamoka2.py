import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv('C:\\Python_ca\\3_dalis\\9\\Mall_Customers.csv')


X = df
# X = pd.get_dummies(X, drop_first=True).astype(int)
# X = X.values
df.set_index('CustomerID', inplace=True)
X = df.iloc[:, [2]].values
print(X)


Z = linkage(X, method ='single')

plt.figure(figsize=(10,7))
dendrogram(Z, labels=df.index)
plt.title('Hierarchical Clustering Dendogram')
plt.xlabel('Simple index')
plt.ylabel('Distance')
plt.show()