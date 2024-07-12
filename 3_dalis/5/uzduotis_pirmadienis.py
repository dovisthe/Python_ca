import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('C:\\Python_ca\\3_dalis\\5\\produktai.csv')

x = df[['Kaina', 'Svoris']]
y = df['Kategorija']

sns.pairplot(df, hue='Kategorija')
plt.show()

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
print(y_encoded)
o = label_encoder.inverse_transform(y_encoded)
print(o)


# x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.3, random_state=42)

# scaler = StandardScaler()
# x_train_scaled = scaler.fit_transform(x_train)
# x_test_scaled = scaler.fit_transform(x_test)

# model = KNeighborsClassifier()
# model.fit(x_train_scaled, y_train)

# # model = RandomForestClassifier(random_state=42)
# # model.fit(x_train_scaled, y_train)

# y_pred = model.predict(x_test_scaled)
# print(classification_report(y_test, y_pred))
# print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# def predict_category(kaina, svoris):
#     prediction = model.predict([[kaina, svoris]])
#     return label_encoder.inverse_transform(prediction)[0]


# new_product = [2,0.9]
# predicted_category = predict_category(*new_product)
# print(f'The predicted category for the new product with price {new_product[0]} EUR and weight {new_product[1]} kg is {predicted_category}.')





# x_min, x_max = x_train_scaled[:, 0].min() - 1, x_train_scaled[:, 0].max() + 1
# y_min, y_max = x_train_scaled[:, 1].min() - 1, x_train_scaled[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)

# plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm)

# plt.scatter(x_train_scaled[:, 0], x_train_scaled[:, 1], c=y_train, s=20, edgecolor='k', cmap=plt.cm.coolwarm, label="Training", marker="o")
# plt.scatter(x_test_scaled[:, 0], x_test_scaled[:, 1], c=y_test, s=50, edgecolor='none',cmap=plt.cm.coolwarm, label="Test", marker="x")
# plt.title("KNN Classification (K=3)")
# plt.xlabel("Feature 1")
# plt.ylabel("Feature 2")
# plt.legend()
# plt.show()
