import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('C:\\Python_ca\\3_dalis\\5\\produktai.csv')

# Exploratory Data Analysis
print(df.head())
print(df.describe())
print(df['Kategorija'].value_counts())

# Visualize the data
sns.pairplot(df, hue='Kategorija')
plt.show()

# Feature and target variables
x = df[['Kaina', 'Svoris']]
y = df['Kategorija']

# Encoding the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(x_train, y_train)

best_model = grid_search.best_estimator_

# Training the model
best_model.fit(x_train, y_train)

# Predictions
y_pred = best_model.predict(x_test)

# Evaluation
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Predict category for a new product
def predict_category(kaina, svoris):
    prediction = best_model.predict([[kaina, svoris]])
    return label_encoder.inverse_transform(prediction)[0]

new_product = [2, 0.9]
predicted_category = predict_category(*new_product)
print(f'The predicted category for the new product with price {new_product[0]} EUR and weight {new_product[1]} kg is {predicted_category}.')