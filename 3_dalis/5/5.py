import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

print(df.head())

df = df.dropna()
x = df.drop("median_house_value", axis=1)
x = pd.get_dummies(x, drop_first=True)
y = df["median_house_value"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

print("LinearRegression")
lin_reg = LinearRegression()
lin_reg.fit(x_train_scaled, y_train)

y_pred_lin = lin_reg.predict(x_test_scaled)

mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)



print(f"MSE: {mse_lin}")
print(f"R2: {r2_lin}")

print("NearestNeighbors")
knn_reg = KNeighborsRegressor()
knn_reg.fit(x_train_scaled, y_train)

y_pred_knn = knn_reg.predict(x_test_scaled)

mse_knn = mean_squared_error(y_test, y_pred_knn)
r2_knn = r2_score(y_test, y_pred_knn)


print(f"MSE: {mse_knn}")
print(f"R2: {r2_knn}")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_lin, alpha=0.5, label='Linijinė regresija')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')
plt.xlabel('Tikrosios reikšmės')
plt.ylabel('Numatytos reikšmės')
plt.title('Tikrosios prieš numatytas reikšmes (Linijinė regresija)')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_knn, alpha=0.5, label='KNN regresorius')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')
plt.xlabel('Tikrosios reikšmės')
plt.ylabel('Numatytos reikšmės')
plt.title('Tikrosios prieš numatytas reikšmes (KNN regresorius)')
plt.legend()
plt.show()

print()
