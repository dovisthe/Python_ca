from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pandas as pd

iris = load_iris()
X, y = iris.data, iris.target

scaler = StandardScaler()

X = scaler.fit_transform(X)

# pd.read_csv('train.csv')
# x_train = train.dop('Target', axis=1)
# y_train = train['Targer']
# x_test = pd.read_csv('test.csv')
# y_test = pd.read_csv('submision.csv')

#train.csv -> x_train and y_train
#test.csv -> x_test
# answers (submission) -> y_test

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42)


nc = KNeighborsClassifier(n_neighbors=7)
nc.fit(x_train, y_train)
y_pred = nc.predict(x_test)
print(accuracy_score(y_test, y_pred))

import seaborn as sns
from matplotlib import pyplot as plt

sns.lineplot(y=y_pred, x=range(0,len(y_pred)))
sns.lineplot(y=y_pred, x=range(0,len(y_pred)))
plt.show()