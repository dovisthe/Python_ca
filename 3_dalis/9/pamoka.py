import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

df = pd.read_csv('C:\\Python_ca\\3_dalis\\9\\Mall_Customers.csv')

# y = df['Spending Score (1-100)']
# X = df.drop(['Spending Score (1-100)',], axis=1)
# X = pd.get_dummies(X, drop_first=True).astype(int)
# X = X.values
X = df.iloc[:, [3,4]].values


print(X)
inertia_values = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    inertia_values.append(kmeans.inertia_)

plt.plot(k_values, inertia_values, 'bx-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

#--Kmeans--------------------------------------------


kmeans = KMeans(n_clusters=4, init ='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)
cluster_centers = kmeans.cluster_centers_

print(y_kmeans)

plt.figure(figsize=(10, 7))

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

print(X)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X')
plt.title('K-means clustering')
plt.xlabel('Income')
plt.ylabel('spending score')
plt.show()

# 2/2 Kmeans-------------------------------

inertia = kmeans.inertia_
silhoutte_avg = silhouette_score(X, y_kmeans)
davies_bouldin = davies_bouldin_score(X, y_kmeans)
calinski_harabasz = calinski_harabasz_score(X, y_kmeans)

print(f'Inertia: {inertia}')
print(f'silhoutte : {silhoutte_avg}')
print(f'davies_bouldin: {davies_bouldin}')
print(f'calinski_harabasz : {calinski_harabasz}')



# from kmodes.kprototypes import KPrototypes

# X = df.iloc[:, 1:].values
# print(X)

# kproto = KPrototypes(n_clusters=5, init='Cao', verbose=1)

# clusters = kproto.fit_predict(X, categorical=[0])

# print(clusters)

# q = kproto.cluster_centroids_

# plt.figure(figsize=(10, 7))
# plt.scatter(X[clusters == 0, 2], X[clusters == 0, 3], s=100, c='red', label='Cluster 1')
# plt.scatter(X[clusters == 1, 2], X[clusters == 1, 3], s=100, c='blue', label='Cluster 2')
# plt.scatter(X[clusters == 2, 2], X[clusters == 2, 3], s=100, c='green', label='Cluster 3')
# plt.scatter(X[clusters == 3, 2], X[clusters == 3, 3], s=100, c='violet', label='Cluster 4')
# plt.scatter(X[clusters == 4, 2], X[clusters == 4, 3], s=100, c='brown', label='Cluster 5')



# plt.title('KPrototypes Clustering')
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.legend()
# plt.show()