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
from sklearn.model_selection import train_test_split

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



#Scaleris----------------------------------------------------------------------------------

# X = df.drop(columns=['SalePrice'])
# y = df['SalePrice']

X_train = df.drop('SalePrice', axis=1)
y_train = df['SalePrice']

X_test = dt
y_test = ss['SalePrice']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#KNN skaiciuojam----------------------------------------------------------------------------------

from sklearn.model_selection import cross_val_score
import numpy as np

k_values = range(1, 31)
cv_score = []

rmse_scorer = make_scorer(mean_squared_error, squared=False)

for k in k_values:
    knn = KNeighborsRegressor(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring=rmse_scorer)
    cv_score.append(scores.mean())

best_k = k_values[np.argmin(cv_score)]
print(f"Best k value: {best_k}")

# sns.lineplot(x = k_values, y = cv_score)
# plt.show()


#SVR-----------------------------

from sklearn.svm import SVR

svr = SVR(kernel='rbf')
svr.fit(X_train, y_train)

y_pred = svr.predict(X_test)




sns.histplot(x=X_test, y=y_pred)
plt.show()








#-Acuracy---------------------------------------------------------------------------------
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=best_k, random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

rmse_rf = mean_squared_error(y_test, y_pred_rf, squared=False)
print(f'Random Forest RMSE: {rmse_rf:.2f}')

r2 = r2_score(y_test, y_pred_rf)
print(f'R² Score: {r2:.2f}')