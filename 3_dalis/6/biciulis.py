import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load datasets
df = pd.read_csv('C:\\Python_ca\\3_dalis\\6\\train.csv')
dt = pd.read_csv('C:\\Python_ca\\3_dalis\\6\\test.csv')
gs = pd.read_csv('C:\\Python_ca\\3_dalis\\6\\sample_submission.csv')

# Add a column to distinguish between train and test
df['is_train'] = 1
dt['is_train'] = 0

# Combine train and test datasets
combined = pd.concat([df, dt], axis=0, ignore_index=True)

# Handle missing values in categorical columns
categorical_cols = combined.select_dtypes(include=['object', 'category']).columns
for column in categorical_cols:
    missing = combined[column].isna().sum()
    percent_missing = (missing / len(combined)) * 100
    if percent_missing <= 40:
        combined[column] = combined[column].fillna(combined[column].mode()[0])
    else:
        combined = combined.drop([column], axis=1)

# Fill missing values in numeric columns
combined['LotFrontage'] = combined['LotFrontage'].fillna(combined['LotFrontage'].mean())
combined['MasVnrArea'] = combined['MasVnrArea'].fillna(combined['MasVnrArea'].mean())
combined['GarageYrBlt'] = combined['GarageYrBlt'].fillna(combined['GarageYrBlt'].mean())

# Encode categorical columns
label_encoder = LabelEncoder()
categorical_cols = combined.select_dtypes(include=['object', 'category']).columns
for column in categorical_cols:
    if combined[column].nunique() <= 10:
        combined[column] = label_encoder.fit_transform(combined[column])
    else:
        combined = pd.get_dummies(combined, columns=[column], drop_first=True)

# Handle outliers in 'LotArea'
Q1 = combined['LotArea'].quantile(0.25)
Q3 = combined['LotArea'].quantile(0.75)
IQR = Q3 - Q1
upper_filter = combined['LotArea'] >= Q3 + 1.5 * IQR
lower_filter = combined['LotArea'] <= Q1 - 1.5 * IQR
combined.loc[upper_filter, 'LotArea'] = Q3 + 1.5 * IQR
combined.loc[lower_filter, 'LotArea'] = Q1 - 1.5 * IQR

# Scale numeric columns
numeric_cols = combined.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
combined[numeric_cols] = scaler.fit_transform(combined[numeric_cols])

# Separate the combined dataset back into train and test sets
df = combined[combined['is_train'] == 1].drop(['is_train'], axis=1)
dt = combined[combined['is_train'] == 0].drop(['is_train'], axis=1)

# Separate target variable from training data
y_train = df['SalePrice']
X_train = df.drop(['SalePrice'], axis=1)

# Ensure test set does not have the target variable
X_test = dt.drop(['SalePrice'], axis=1, errors='ignore')

# Train a RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Prepare the submission file
gs['SalePrice'] = predictions
gs.to_csv('C:\\Python_ca\\3_dalis\\6\\submission.csv', index=False)