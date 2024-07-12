import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=500, n_features=2, n_informative=2, n_redundant=0, random_state=10)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

knn = KNeighborsClassifier(n_neighbors=10, metric="minkowski", algorithm="auto", weights="distance")
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

report = classification_report(y_test, y_pred)

print(report)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.03), np.arange(y_min, y_max, 0.03))


Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm)

plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, s=20, edgecolor='k', cmap=plt.cm.coolwarm, label="Training")
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test, s=50, edgecolor='none',cmap=plt.cm.coolwarm, label="Test")
plt.title("KNN Classification (K=3)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
