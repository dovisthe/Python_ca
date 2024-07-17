import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor, GradientBoostingRegressor, VotingRegressor, AdaBoostRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('C:\\Python_ca\\3_dalis\\atsiskaitymas\\london_merged.csv')

# Padaraome is timestamp menesi, diena ir valanda
df['timestamp'] = pd.to_datetime(df['timestamp'])

df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['Hour'] = df['timestamp'].dt.hour
df['dayofweek'] = df['timestamp'].dt.dayofweek
 

# Istrinam timestamp columa, nes nebereikia
#istriname actual temp, pagereja tikslumas spejimo, todel manome, kad uztenka ir gal net svarbiau koks jausmas oro negu tikra temp

df = df.drop(['timestamp', 't1'], axis=1)

# Padarome One-hot encodinima
df = pd.get_dummies(df, drop_first=True)


#---------Paziurim ar nera outlieriu labai isplaukusiu, bet visiskai skirtumo nedave sitas, todel nusprendem uzkomentuoti-------------------
# sns.catplot(y=df['cnt'])
# plt.show()

# Q1 = df['cnt'].quantile(0.25)
# Q3 = df['cnt'].quantile(0.75)
# IQR = Q3 - Q1   
# upperFilter = (df['cnt'] >= Q3 + 1.5 * IQR)
# df.loc[upperFilter,['cnt']]  = Q3 + 1.5 * IQR
# df['cnt'].fillna(df['cnt'].mean(), inplace=True)


x = df.drop('cnt', axis=1)
y = df['cnt']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

#Scalinam x, kad suvienodintu skaiciukus
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)


#Darome XGBRegressor---------------------------------------------------------------------------------------------------

xgbr = XGBRegressor(
    random_state=42,
    learning_rate=0.1,
    n_estimators=200,
)

param_grid = {
    # 'n_estimators': [50, 100, 150, 200, 250, 300],
    # 'learning_rate': [0.01, 0.05, 0.1, 0.2, 0.3],
}

grid_search = GridSearchCV(estimator=xgbr, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
grid_search.fit(x_train_scaled, y_train)

xgbr_best = grid_search.best_estimator_

y_pred = xgbr_best.predict(x_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)

print('-'*100)
print('-'*100)
print('XGBRegressor Rezultatai:')
print(f"RMSE : {rmse}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")
print('-'*100)
print('-'*100)

#RandomFore----------------------------------------------------

rf = RandomForestRegressor(n_estimators=147,max_depth=21,min_samples_leaf=1, min_samples_split=4,random_state=42,oob_score=True)
rf.fit(x_train_scaled, y_train)

y_pred = rf.predict(x_test_scaled)

params = {
    # 'n_estimators': [50, 100, 150, 200],
    # 'max_features': [1, 2, 3, 4, 5]
}

grid_search = GridSearchCV(rf, params, scoring="neg_mean_squared_error", cv=5)
grid_search.fit(x_train_scaled, y_train)

rf_best = grid_search.best_estimator_

y_pred_best = rf_best.predict(x_test_scaled)


mse_rfr = root_mean_squared_error(y_test, y_pred_best)
r2_rfr = r2_score(y_test, y_pred_best)
rmse_rfr= np.sqrt(mse_rfr)


print('RandomForestRegressor Rezultatai:')
print(f"RMSE Rfr: {rmse_rfr}")
print(f"Mean Squared Error: {mse_rfr}")
print(f"R-squared Score: {r2_rfr}")
print('-'*100)
print('-'*100)
#-----Grafikai------

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_best, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title('RandomForestRegressor Actual vs Predicted Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.grid()

plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title('XGBRegressor Actual vs Predicted Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.grid()
plt.tight_layout()
plt.show()


#-HEATMAP
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

