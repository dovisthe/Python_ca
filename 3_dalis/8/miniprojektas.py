import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor, GradientBoostingRegressor, VotingRegressor, AdaBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

df = pd.read_csv('C:\\Python_ca\\3_dalis\\8\\Student_performance_data _.csv')

x = df.drop('GPA', axis=1)
y = df['GPA']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

df = df.drop(columns=['Ethnicity', 'ParentalEducation', 'Volunteering'])
#------------------------------------------------------------

# rf = RandomForestRegressor(max_features=5, n_estimators=49, random_state=42)
# rf.fit(x_train, y_train)
# y_pred = rf.predict(x_test)

# rmse = mean_squared_error(y_test, y_pred, squared=False)
# print(f"Root Mean Squared Error: {rmse}")

# params = {
#     'n_estimators': range(1, 51),
#     'max_features': [1, 2, 3, 4, 5]
# }

# grid_search = GridSearchCV(rf, params, scoring="neg_mean_squared_error", cv=5)
# grid_search.fit(x_train, y_train)

# rf_best = grid_search.best_estimator_

# y_pred = rf_best.predict(x_test)

# rmse = mean_squared_error(y_test, y_pred, squared=False)
# print(f"Root Mean Squared Error: {rmse}")
# print(f"Best Parameters: {grid_search.best_params_}")

#BaggingRegressor------------------------------------------------------------------------------------

# base_estimator = DecisionTreeRegressor(random_state=42)

# bagging_regressor = BaggingRegressor(estimator=base_estimator, random_state=42, bootstrap=True, bootstrap_features=False, max_features=1.0, max_samples=0.7, n_estimators=200)

# param_grid = {
#     'n_estimators': range(50, 201, 50),
#     'max_features': [0.5, 0.7, 1.0],
#     'max_samples': [0.5, 0.7, 1.0],
#     'bootstrap': [True, False],
#     'bootstrap_features': [True, False]
# }

# grid_search = GridSearchCV(bagging_regressor, param_grid, scoring="neg_mean_squared_error", cv=5)
# grid_search.fit(x_train, y_train)

# best_bagging = grid_search.best_estimator_

# y_pred_best = best_bagging.predict(x_test)

# rmse_best = mean_squared_error(y_test, y_pred_best, squared=False)
# print(f"Best Model Root Mean Squared Error: {rmse_best}")
# print(f"Best Parameters: {grid_search.best_params_}")

#GradientBoostingRegressor--------------------------------------------------------------------------------------

gbr = GradientBoostingRegressor(random_state=42, learning_rate=0.1, max_depth=4, n_estimators=103)

param_grid = {
    # 'n_estimators': [50, 100, 150, 200],
    # 'max_depth': [3, 4, 5, 6],
    # 'learning_rate': [0.01, 0.05, 0.1, 0.2],
    # 'subsample': [0.8, 0.9, 1.0],
    # 'max_features': ['auto', 'sqrt', 'log2']
}

grid_search = GridSearchCV(estimator=gbr, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
grid_search.fit(x_train, y_train)

gbr_best = grid_search.best_estimator_

y_pred = gbr_best.predict(x_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)

r2 = r2_score(y_test, y_pred)

print(f"Best Model Root Mean Squared Error: {rmse}")
print(f"Best Parameters: {grid_search.best_params_}")
print(f"R² Score: {r2}")

#SVR--------------------------------------------

# from sklearn.svm import SVR

# svr = SVR()

# # Perform GridSearchCV to find the best parameters
# params = {
#     'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
#     'C': [0.1, 1, 10, 23, 50, 100],
#     'gamma': ['scale', 'auto', 0.01, 0.1, 1, 10]
# }

# grid_search = GridSearchCV(svr, params, scoring="neg_mean_squared_error", cv=5)
# grid_search.fit(x_train, y_train)

# # Get the best model from grid search
# svr_best = grid_search.best_estimator_

# # Make predictions with the best model
# y_pred_best = svr_best.predict(x_test)

# # Calculate and print the RMSE for the best model
# rmse_best = mean_squared_error(y_test, y_pred_best, squared=False)
# print(f"Best Model Root Mean Squared Error: {rmse_best}")
# print(f"Best Parameters: {grid_search.best_params_}")

#XGBRegressor--------------------------------------------------------

xgbr= XGBRegressor(
    random_state=42,
    colsample_bytree=0.9,
    learning_rate=0.05,
    max_depth=4,
    n_estimators=200,
    subsample=0.8
)

param_grid = {
    # 'n_estimators': [50, 100, 150, 200],
    # 'max_depth': [3, 4, 5, 6],
    # 'learning_rate': [0.01, 0.05, 0.1, 0.2],
    # 'subsample': [0.8, 0.9, 1.0],
    # 'colsample_bytree': [0.8, 0.9, 1.0]
}

grid_search = GridSearchCV(estimator=xgbr, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
grid_search.fit(x_train, y_train)

xgbr_best = grid_search.best_estimator_

y_pred = xgbr_best.predict(x_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)

r2 = r2_score(y_test, y_pred)

print(f"Best Model Root Mean Squared Error: {rmse}")
print(f"Best Parameters: {grid_search.best_params_}")
print(f"R² Score: {r2}")

#ADA--------------------------------------------------------------

# adaboost = AdaBoostRegressor(random_state=42)

# param_grid = {
#     'n_estimators': [50, 100, 150, 200],
#     'learning_rate': [0.01, 0.1, 0.5, 1.0]
# }

# grid_search = GridSearchCV(estimator=adaboost, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)

# grid_search.fit(x_train, y_train)

# adaboost_best = grid_search.best_estimator_

# y_pred = adaboost_best.predict(x_test)

# rmse = mean_squared_error(y_test, y_pred, squared=False)

# print(f"Best AdaBoost Model RMSE: {rmse}")
# print(f"Best Parameters: {grid_search.best_params_}")

#VOTING-------------------------------------------------------------

# voting_regressor = VotingRegressor(estimators=[
#     ('ada', AdaBoostRegressor(random_state=42, n_estimators=100, learning_rate=0.1)),
#     ('rf', RandomForestRegressor(random_state=42, max_depth=5, n_estimators=100))
# ])

# param_grid = {
#     'ada__n_estimators': [50, 100],
#     'ada__learning_rate': [0.01, 0.1],
#     'rf__n_estimators': [50, 100],
#     'rf__max_depth': [3, 5]
# }

# grid_search = GridSearchCV(estimator=voting_regressor, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
# grid_search.fit(x_train, y_train)

# best_model = grid_search.best_estimator_
# y_pred = best_model.predict(x_test)
# rmse = mean_squared_error(y_test, y_pred, squared=False)

# print(f"Best Model RMSE: {rmse}")
# print(f"Best Parameters: {grid_search.best_params_}")