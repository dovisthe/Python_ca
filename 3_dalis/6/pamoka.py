import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

np.random.seed(42)

data = pd.DataFrame({
    'x1': np.random.rand(100),
    'x2': np.random.rand(100) * 5,
    'x3': np.random.rand(100) * 10,
    'x4': np.random.rand(100) * 20
})

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

pca = PCA(2)
principal_components = pca.fit_transform(scaled_data)

df_PCA = pd.DataFrame(data = principal_components, columns=["PC1", "PC2"])

explained_variance = pca.explained_variance_ratio_

print(explained_variance)


