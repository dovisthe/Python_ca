import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv'

df = pd.read_csv(url)

print(df.head())

df.dropna()
x = df.drop("median_house_value", axis=1)
x = pd.get_dummies(x, drop_first=True)
y = df["median_house_value"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

print()

lin_reg = LinearRegression()
lin_reg.fit(x_test_scaled, y_train)

y_pred_lin = lin_reg.predict(x_test_scaled)

mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

print(f"MSE: {mse_lin}")
print(f"R2: {r2_lin}")


print()