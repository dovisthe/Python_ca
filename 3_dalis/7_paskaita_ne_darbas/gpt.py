import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('C:\\Python_ca\\3_dalis\\7_paskaita_ne_darbas\\train.csv')
dt = pd.read_csv('C:\\Python_ca\\3_dalis\\7_paskaita_ne_darbas\\test.csv')
ss = pd.read_csv('C:\\Python_ca\\3_dalis\\7_paskaita_ne_darbas\\sample_submission.csv')

# Drop specified columns
columns_to_drop = ['Street', 'Alley', 'Utilities', 'LandSlope', 'Condition2', 'RoofMatl',
                   'MasVnrArea', 'BsmtCond', 'BsmtFinSF2', 'Heating', 'Electrical',
                   'LowQualFinSF', 'BsmtHalfBath', 'KitchenAbvGr', 'Functional',
                   'GarageYrBlt', 'GarageQual', 'GarageCond', 'PavedDrive', '3SsnPorch',
                   'ScreenPorch', 'PoolQC', 'MiscFeature', 'MiscVal', 'Neighborhood',
                   'MSZoning', 'LotShape', 'LandContour', 'Condition1', 'BldgType',
                   'RoofStyle', 'Exterior1st', 'Exterior2nd', 'HouseStyle', 'SaleCondition',
                   'SaleType', 'GarageType', 'BsmtFinType1', 'ExterCond', 'BsmtExposure',
                   'BsmtFinType2', 'HeatingQC', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 
                   'BsmtFullBath', 'PoolArea', 'MoSold', 'YrSold']

df.drop(columns=columns_to_drop, inplace=True)
dt.drop(columns=columns_to_drop, inplace=True)

# Handle missing values in categorical columns
for column in df.select_dtypes(include=['object', 'category']).columns:
    if df[column].isna().sum() / len(df) <= 0.40:
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        df.drop(columns=[column], inplace=True)

# Handle missing values in numerical columns
df['LotFrontage'].fillna(df['LotFrontage'].mean(), inplace=True)
df.fillna(df.mean(), inplace=True)

# Convert categorical columns to dummy variables
df = pd.get_dummies(df, drop_first=True)
dt = pd.get_dummies(dt, drop_first=True)

# Ensure that dt has the same columns as df
dt = dt.reindex(columns=df.columns.drop('SalePrice'), fill_value=0)

# Remove outliers in 'LotArea'
Q1 = df['LotArea'].quantile(0.25)
Q3 = df['LotArea'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR
df.loc[df['LotArea'] > upper_bound, 'LotArea'] = upper_bound
df.loc[df['LotArea'] < lower_bound, 'LotArea'] = lower_bound

# Remove specific IDs from dt and ss
ids_to_remove = [2121, 2189, 2577]
dt = dt[~dt['Id'].isin(ids_to_remove)]
ss = ss[~ss['Id'].isin(ids_to_remove)]

# Prepare training and testing datasets
X_train = df.drop('SalePrice', axis=1)
y_train = df['SalePrice']
X_test = dt

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN Model
def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

k_values = range(1, 31)
cv_scores = []

rmse_scorer = make_scorer(root_mean_squared_error, greater_is_better=False)

for k in k_values:
    knn = KNeighborsRegressor(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring=rmse_scorer)
    cv_scores.append(scores.mean())

best_k = k_values[np.argmin(cv_scores)]
print(f"Best k value: {best_k}")

knn_best = KNeighborsRegressor(n_neighbors=best_k)
knn_best.fit(X_train, y_train)
y_pred_knn = knn_best.predict(X_test)

# SVR Model
svr = SVR(kernel='rbf', C=1.0)
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)

# Decision Tree Model
tree = DecisionTreeRegressor(max_depth=3, min_samples_split=4, min_samples_leaf=2)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)

# Actual vs Predicted plots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# KNN plot
axs[0].scatter(ss['SalePrice'], y_pred_knn, alpha=0.5)
axs[0].plot([ss['SalePrice'].min(), ss['SalePrice'].max()], [ss['SalePrice'].min(), ss['SalePrice'].max()], 'k--', lw=2)
axs[0].set_xlabel('Actual Price')
axs[0].set_ylabel('Predicted Price')
axs[0].set_title('Actual Price vs. Predicted Price (KNN)')

# SVR plot
axs[1].scatter(ss['SalePrice'], y_pred_svr, alpha=0.5)
axs[1].plot([ss['SalePrice'].min(), ss['SalePrice'].max()], [ss['SalePrice'].min(), ss['SalePrice'].max()], 'k--', lw=2)
axs[1].set_xlabel('Actual Price')
axs[1].set_ylabel('Predicted Price')
axs[1].set_title('Actual Price vs. Predicted Price (SVR)')

# Decision Tree plot
axs[2].scatter(ss['SalePrice'], y_pred_tree, alpha=0.5)
axs[2].plot([ss['SalePrice'].min(), ss['SalePrice'].max()], [ss['SalePrice'].min(), ss['SalePrice'].max()], 'k--', lw=2)
axs[2].set_xlabel('Actual Price')
axs[2].set_ylabel('Predicted Price')
axs[2].set_title('Actual Price vs. Predicted Price (Decision Tree)')

plt.tight_layout()
plt.show()