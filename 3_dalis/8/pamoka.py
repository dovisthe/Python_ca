import pandas as pd
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

iris = load_wine()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["species"] = iris.target

x = df.drop('species', axis=1)
y = df['species']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)

params = {
    'n_estimators': range(1,50),
    'max_features': range(1,5)
}

base_mode = DecisionTreeClassifier()
# rf = RandomForestClassifier(n_estimators=50, random_state=42)
# rf.fit(x_train, y_train)
# y_pred = rf.predict(x_test)


rf = BaggingClassifier(base_mode, n_estimators=11, max_features=3, random_state=42)


grid_search = GridSearchCV(rf, params, scoring="accuracy")
grid_search.fit(x_train, y_train)
rf_best = grid_search.best_estimator_
print(rf_best)

# rf.fit(x_train, y_train)
# y_pred = rf.predict(x_test)

# accuracy = accuracy_score(y_test, y_pred)
# print(accuracy)



