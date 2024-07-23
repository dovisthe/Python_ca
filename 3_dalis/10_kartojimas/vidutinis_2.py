import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler

#Įkelkite CSV failą su istorinių orų duomenimis (data, temperatūra, krituliai).

df = pd.read_csv('C:\\Python_ca\\3_dalis\\10_kartojimas\\kaunas_weather.csv')


# column_std = np.std(df, axis=0)
# print(column_std)
print(df.describe())

df['datetime'] = pd.to_datetime(df['datetime'])

df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day

df = df.drop(['datetime', 'snow', 'feelslike', 'dew'], axis=1)

df = pd.get_dummies(df, drop_first=True)
df = df.fillna(df.mean())

print(df.info())
print(df.head())
print(df.std())

x2 = df.groupby("month")['temp'].mean()
print(x2)

