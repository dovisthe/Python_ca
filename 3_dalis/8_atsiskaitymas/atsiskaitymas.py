import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import root_mean_squared_error, r2_score
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

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
# df = pd.get_dummies(df, drop_first=True)

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
    # 'n_estimators': [100, 150, 200, 250],
    # 'learning_rate': [0.01, 0.05, 0.1, 0.2],
    # 'max_depth': [3, 5, 7, 9],
}

grid_search = GridSearchCV(estimator=xgbr, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5)
grid_search.fit(x_train_scaled, y_train)

xgbr_best = grid_search.best_estimator_

y_pred = xgbr_best.predict(x_test_scaled)

r2 = r2_score(y_test, y_pred)
rmse_x = root_mean_squared_error(y_test, y_pred)

print('-'*100)
print('-'*100)
print('XGBRegressor Results:')
print(f"RMSE : {rmse_x}")
print(f"R-squared Score: {r2}")
print('-'*100)
print('-'*100)

#GradientBoostingRegressor----------------------------------------------------

gb = GradientBoostingRegressor(n_estimators=120,min_samples_split= 4,min_samples_leaf= 15, learning_rate=0.1, max_depth=15,random_state=42)
gb.fit(x_train_scaled, y_train)
y_pred_gb = gb.predict(x_test_scaled)

params = {
    # 'n_estimators': [50, 100, 150, 200],
    # 'max_features': [1, 2, 3, 4, 5]
}

grid_search = GridSearchCV(gb, params, scoring="neg_mean_squared_error", cv=5)
grid_search.fit(x_train_scaled, y_train)

gb_best = grid_search.best_estimator_

y_pred_best = gb_best.predict(x_test_scaled)

rmse_rfr = root_mean_squared_error(y_test, y_pred_best)
r2_rfr = r2_score(y_test, y_pred_best)

print('GradientBoostingRegressor Results:')
print(f"RMSE : {rmse_rfr}")
print(f"R-squared Score: {r2_rfr}")
print('-'*100)
print('-'*100)


# #-----Grafikai palyginti kaip speja
# sns.set_theme(style="darkgrid")

# plt.subplot(1, 2, 1)
# plt.scatter(y_test, y_pred_best, alpha=0.7)
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
# plt.title('GradientBoostingRegressor: Actual vs Predicted Values')
# plt.xlabel('Actual Values')
# plt.ylabel('Predicted Values')
# plt.grid()

# plt.subplot(1, 2, 2)
# plt.scatter(y_test, y_pred, alpha=0.7)
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
# plt.title('XGBRegressor: Actual vs Predicted Values')
# plt.xlabel('Actual Values')
# plt.ylabel('Predicted Values')
# plt.grid()
# plt.tight_layout()
# plt.show()


# #-HEATMAP, matome kas daugiausiai itakoja nuom, izvalga
# plt.figure(figsize=(10, 8))
# correlation_matrix = df.corr()
# plt.subplots_adjust(bottom=0.15)
# sns.heatmap(correlation_matrix, annot=True,fmt=".2f", cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Heatmap')
# plt.show()

# #sukuriam predictinta count
# df_pred = pd.DataFrame({'year': x_test['year'],
#                         'month': x_test['month'],
#                         'Hour': x_test['Hour'],
#                         'weather_code': x_test['weather_code'],
#                         'cnt': y_pred_best}
#                         )


# # Izvalga kaip valandos itakoja nuoma, ir kaip redictina

# plt.figure(figsize=(14, 6))
# plt.subplot(1, 2, 1)
# sns.barplot(x=df['Hour'], y=y_pred_gb)
# plt.title('Rented bike avarage count based on Hour')
# plt.xlabel('Hour')
# plt.ylabel('Count')

# plt.subplot(1, 2, 2)
# sns.barplot(x=x_test['hour'], y='cnt')
# plt.title('Rented bike avarage count based on Hour - Predicted')
# plt.xlabel('Hour')
# plt.ylabel('Count')

# plt.tight_layout()
# plt.show()

# # Izvalga kaip oro salygos itakoja nuoma, ir kaip predictina
# plt.figure(figsize=(14, 6))
# plt.subplot(1, 2, 1)
# sns.barplot(data=df, x='weather_code', y='cnt')
# plt.title('Rented bike avarage count based on weather')
# plt.xlabel('Weather code')
# plt.ylabel('Count')

# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0, 1, 2, 3, 4, 5, 6]
# labels = ['Clear', 'few clouds', 'Broken clouds ', 'Cloudy', 'Rain', 'thunderstorm', 'snowfall ']
# plt.plot(x, y)
# plt.xticks(x, labels)

# plt.subplot(1, 2, 2)
# sns.barplot(data=df_pred, x='weather_code', y='cnt')
# plt.title('Rented bike avarage count based on weather -  Predicted')
# plt.xlabel('Weather code')
# plt.ylabel('Count')

# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0, 1, 2, 3, 4, 5, 6]
# labels = ['Clear', 'few clouds', 'Broken clouds ', 'Cloudy', 'Rain', 'thunderstorm', 'snowfall ']
# plt.plot(x, y)
# plt.xticks(x, labels)

# plt.tight_layout()
# plt.show()


#LInegraph pabandyti.
#pagal sezonus paskaiciuioti counta,

plt.figure(figsize=(14, 6))
sns.barplot(data=df, x='season', y='cnt')
plt.title('Rented bike avarage count based on Season')
plt.xlabel('Seasons')
plt.ylabel('Count')
x = [0, 1, 2, 3]
y = [0, 1, 2, 3]
labels = ['Spring', 'Summer', 'Fall', 'Winter']
plt.plot(x, y)
plt.xticks(x, labels)
plt.show()



plt.figure(figsize=(14, 7))

plt.plot(y_test.values, label='Actual', color='black', linestyle='dotted')
# plt.plot(y_pred, label='XGBRegressor Predictions', color='blue')
plt.plot(y_pred_best, label='GradientBoostingRegressor Predictions', color='green')

plt.title('Actual vs Predicted Bike Counts')
plt.xlabel('Index')
plt.ylabel('Count')
plt.legend()
plt.show()

