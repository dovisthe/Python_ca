import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

data = load_wine()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

inertia_values = []
k_values = range(1, 21)

for k in k_values:
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=20, random_state=0)
    kmeans.fit(X_train_scaled)
    inertia_values.append(kmeans.inertia_)

plt.plot(k_values, inertia_values, 'bx-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=20, random_state=0)
y_kmeans = kmeans.fit_predict(X_train_scaled)
cluster_centers = kmeans.cluster_centers_


plt.figure(figsize=(10, 7))

plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_kmeans, s=50, cmap='viridis')

plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X')
plt.title('K-means clustering')
plt.xlabel('Feature 1 (Standardized)')
plt.ylabel('Feature 2 (Standardized)')
plt.show()