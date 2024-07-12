from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import classification_report, accuracy_score, mean_squared_error, r2_score, make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, make_scorer, mean_squared_error as mse
from sklearn.metrics import root_mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_squared_error as mse
from sklearn.metrics import mean_squared_error as rmse



# svc -svr

df = pd.read_csv('C:\\Python_ca\\3_dalis\\7_paskaita_ne_darbas\\train.csv')
dt = pd.read_csv('C:\\Python_ca\\3_dalis\\7_paskaita_ne_darbas\\test.csv')
ss = pd.read_csv('C:\\Python_ca\\3_dalis\\7_paskaita_ne_darbas\\sample_submission.csv')

#Train.csv ------------------------------------

df = df.drop(columns=['Street', 'Alley', 'Utilities', 'LandSlope', 'Condition2', 'RoofMatl',
                      'MasVnrArea', 'BsmtCond', 'BsmtFinSF2', 'Heating', 'Electrical',
                      'LowQualFinSF', 'BsmtHalfBath', 'KitchenAbvGr', 'Functional',
                      'GarageYrBlt', 'GarageQual', 'GarageCond', 'PavedDrive', '3SsnPorch',
                      'ScreenPorch', 'PoolQC', 'MiscFeature', 'MiscVal', 'Neighborhood',
                      'MSZoning', 'LotShape', 'LandContour', 'Condition1', 'BldgType',
                      'RoofStyle', 'Exterior1st', 'Exterior2nd', 'HouseStyle'
                      ])


categorical_cols = df.select_dtypes(include=['object', 'category']).columns

for column in categorical_cols:
    missing = df[column].isna().sum()
    percent_missing = (missing / len(df)) * 100
    if 40 >= percent_missing:
        df[column] = df[column].fillna(df[column].mode()[0])
    else:
        df = df.drop([column], axis=1)

df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

for column in numeric_cols:
    df[column] = df[column].fillna(df[column].mean())

categorical_cols = df.select_dtypes(include=['object', 'category']).columns

for column in categorical_cols:
    df = pd.get_dummies(df, columns=[column], drop_first=True)
 
Q1 = df['LotArea'].quantile(0.25)
Q3 = df['LotArea'].quantile(0.75)
IQR = Q3 - Q1  
upperFilter = (df['LotArea'] >= Q3 + 1.5 *IQR)
lowerFilter = (df['LotArea'] <= Q1 - 1.5 *IQR)
df.loc[upperFilter,['LotArea']]  = Q3 + 1.5 *IQR
df.loc[lowerFilter,['LotArea']]  = Q1 - 1.5 *IQR

#test.cv-------------------------------------------------------------------
dt = dt.drop(columns=['Street', 'Alley', 'Utilities', 'LandSlope', 'Condition2', 'RoofMatl',
                      'MasVnrArea', 'BsmtCond', 'BsmtFinSF2', 'Heating', 'Electrical',
                      'LowQualFinSF', 'BsmtHalfBath', 'KitchenAbvGr', 'Functional',
                      'GarageYrBlt', 'GarageQual', 'GarageCond', 'PavedDrive', '3SsnPorch',
                      'ScreenPorch', 'PoolQC', 'MiscFeature', 'MiscVal', 'Neighborhood',
                      'MSZoning', 'LotShape', 'LandContour', 'Condition1', 'BldgType',
                      'RoofStyle', 'Exterior1st', 'Exterior2nd', 'HouseStyle'
                      ])


categorical_cols = dt.select_dtypes(include=['object', 'category']).columns

for column in categorical_cols:
    missing = dt[column].isna().sum()
    percent_missing = (missing / len(dt)) * 100
    if 40 >= percent_missing:
        dt[column] = dt[column].fillna(dt[column].mode()[0])
    else:
        dt = dt.drop([column], axis=1)

dt['LotFrontage'] = dt['LotFrontage'].fillna(dt['LotFrontage'].mean())

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

for column in numeric_cols:
    df[column] = df[column].fillna(df[column].mean())
       

categorical_cols = dt.select_dtypes(include=['object', 'category']).columns

for column in categorical_cols:
    dt = pd.get_dummies(dt, columns=[column], drop_first=True)
 
Q1 = dt['LotArea'].quantile(0.25)
Q3 = dt['LotArea'].quantile(0.75)
IQR = Q3 - Q1  
upperFilter = (dt['LotArea'] >= Q3 + 1.5 *IQR)
lowerFilter = (dt['LotArea'] <= Q1 - 1.5 *IQR)
dt.loc[upperFilter,['LotArea']]  = Q3 + 1.5 *IQR
dt.loc[lowerFilter,['LotArea']]  = Q1 - 1.5 *IQR

dt = dt[dt['Id'] != 2121]
dt = dt[dt['Id'] != 2189]
dt = dt[dt['Id'] != 2577]


#SS.cvs----------------------------------------------------------------------------
ss = ss[ss['Id'] != 2121]
ss = ss[ss['Id'] != 2189]
ss = ss[ss['Id'] != 2577]


#Scaleris----------------------------------------------------------------------------------

X_train = df.drop('SalePrice', axis=1)
y_train = df['SalePrice']

X_test = dt
y_test = ss['SalePrice']

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#KNN skaiciuojam----------------------------------------------------------------------------------
k_values = range(1, 31)
cv_scores = []

rmse_scorer = make_scorer(root_mean_squared_error)

for k in k_values:
    knn = KNeighborsRegressor(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring=rmse_scorer)
    cv_scores.append(scores.mean())

best_k = k_values[np.argmin(cv_scores)]
print(f"Best k value: {best_k}")

#SVR-----------------------------

dt.to_csv('kasciadarosi.csv', index=False)

from sklearn.svm import SVR

svr = SVR(kernel='rbf')
svr.fit(X_train, y_train)

y_pred = svr.predict(X_test)

#-Tree-----------------------------------------------

from sklearn.tree import DecisionTreeRegressor

# tree = DecisionTreeRegressor(random_state=11)
# tree.fit(X_train, y_train)
# y_pred = tree.predict(X_test)

#-Acuracy---------------------------------------------------------------------------------

rf = RandomForestRegressor(n_estimators=best_k, random_state=11)
# rf.fit(X_train, y_train)

# y_pred_rf = rf.predict(X_test)

rmse_rf = mse(y_test, y_pred, squared=False)

print(f'Random Forest RMSE: {rmse_rf:.2f}')

r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2:.2f}')