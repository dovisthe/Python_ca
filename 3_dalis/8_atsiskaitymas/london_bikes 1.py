import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, make_scorer
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

green_color = '\033[92m'
reset_color = '\033[0m'

df = pd.read_csv('london_merged.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['hour'] = df['timestamp'].dt.hour
df['dayofweek'] = df['timestamp'].dt.dayofweek

df = df.drop('timestamp', axis=1)

x = df.drop('cnt', axis=1)
y = df['cnt']
# print(df.head(60))
# sns.catplot(y=df['cnt'])
# plt.show()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.fit_transform(x_test)

################################################################ RandomForestRegressor
print('-'*181)
print('-'*79, 'RandomForestRegressor','-'*79)

rfr = RandomForestRegressor(n_estimators=147,max_depth=21,min_samples_leaf=1, min_samples_split=4,random_state=42,oob_score=True)
rfr.fit(X_train_scaled, y_train)
y_pred_rfr = rfr.predict(X_test_scaled)

mse_rfr = mean_squared_error(y_test, y_pred_rfr)
r2_rfr = r2_score(y_test, y_pred_rfr)
rmse_rfr= np.sqrt(mse_rfr)

print(f"oob  SCORE:\n{rfr.oob_score_}")
print(f"RMSE Rfr: {rmse_rfr:.4f}")
print(f"Mean Squared Error: {mse_rfr:.4f}")
print(f"R-squared Score: {green_color}{r2_rfr:.4f}{reset_color}")


################################################################## GradientBoostingRegressor
print('-'*181)
print('-'*77, 'GradientBoostingRegressor','-'*77)

gb_regressor = GradientBoostingRegressor(n_estimators=120,min_samples_split= 4,min_samples_leaf= 15, learning_rate=0.1, max_depth=15,random_state=42)
gb_regressor.fit(X_train_scaled, y_train)
y_pred_gb = gb_regressor.predict(X_test_scaled)

mseGB = mean_squared_error(y_test, y_pred_gb)
r2GB = r2_score(y_test, y_pred_gb)
rmseGB= np.sqrt(mseGB)

print(f"RMSE GB: {rmseGB:.4f}")
print(f"Mean Squared Error GB: {mseGB:.4f}")
print(f"R-squared Score GB: {green_color}{r2GB:.3f}{reset_color}")

################################################################## XGBRegressor
print('-'*181)
print('-'*83, 'XGBRegressor ','-'*83)

# xgbr = XGBRegressor(
#     random_state=42,
# )

# param_grid = {
#     'n_estimators': [50, 100, 150, 200],
#     'max_depth': [3, 4, 5, 6,10,12,15],
#     'learning_rate': [0.01, 0.05, 0.1, 0.2],
#     'subsample': [0.8, 0.9, 1.0],
#     # 'colsample_bytree': [0.8, 0.9, 1.0]
# }

# grid_search = GridSearchCV(estimator=xgbr, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
# grid_search.fit(X_train_scaled, y_train) #### pa

# xgbr_best = grid_search.best_estimator_

# y_pred = xgbr_best.predict(X_test_scaled)

# rmse = mean_squared_error(y_test, y_pred, squared=False)
# r2 = r2_score(y_test, y_pred)

# print(f"Best Model Root Mean Squared Error: {rmse}")
# print(f"Best Parameters: {grid_search.best_params_}")
# print(f"R² Score: {green_color}{r2}{reset_color}")

# Best Parameters: {}'learning_rate': 0.05, 'max_depth': 10, 'n_estimators': 200, 'subsample': 0.8

XGB_reg = XGBRegressor(learning_rate=0.05, max_depth=9, n_estimators=200,subsample=0.8,randomstate=42)
XGB_reg.fit(X_train_scaled, y_train)
y_pred_XGB = XGB_reg.predict(X_test_scaled)

XGB_mse = mean_squared_error(y_test, y_pred_XGB)
XGB_r2 = r2_score(y_test, y_pred_XGB)
rmse_XGB= np.sqrt(XGB_mse)

print(f"RMSE XGB: {rmse_XGB:.4f}")
print("XGBBoost MSE:", XGB_mse)
print(f"XGBBoost R2 Score: {green_color}{XGB_r2:.3f}{reset_color}")

################################# Grafikai

df_pred = pd.DataFrame({'year': x_test['year'],
                        'month': x_test['month'],
                        'hour': x_test['hour'],
                        'cnt': y_pred_XGB}
                        )


plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.barplot(data=df, x='hour', y='cnt')
plt.title('Rented by hour Actual')
plt.xlabel('Hour')
plt.ylabel('cnt')
# plt.show()

plt.subplot(1, 2, 2)
sns.barplot(data=df_pred, x='hour', y='cnt')
plt.title('Rented bikes by hour XGBoost Predicted')
plt.xlabel('Hour')
plt.ylabel('cnt')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 6))
# Random Forest plot
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_gb, color='blue', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Faktinis cnt')
plt.ylabel('Prognozuotas cnt')
plt.title('gb Prognozės')

# XGBoost plot 
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_XGB, color='green', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Faktinis Cnt')
plt.ylabel('Prognozuotas cnt')
plt.title('XGBoost Prognozės')

plt.tight_layout()
plt.show()

# print("-"*181)
# print('-'*81, 'Padarytos isvados','-'*81)
# print()

