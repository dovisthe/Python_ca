import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Python_ca\\3_dalis\\3\\train.csv')
df = df.drop(["PassengerId", 'Name', 'Cabin', 'Ticket'], axis=1)

df['Age'].fillna(df['Age'].mean(), inplace=True)

df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

x = df.drop('Survived', axis=1)
y = df["Survived"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=11)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

log_reg = LogisticRegression()
log_reg.fit(x_train_scaled, y_train)

y_pred_log = log_reg.predict(x_test_scaled)

accuracy = accuracy_score(y_test, y_pred_log)
conf_mat = confusion_matrix(y_test, y_pred_log)
classificatio = classification_report(y_test, y_pred_log)

print("----------------------------------")

print(classificatio)
print("Logistic Regression")
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_mat)

print("----------------------------------")

plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt="d", cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix for Logistic Regression')
plt.show()

print("----------------------------------")

print(df.head())
# Faktiniai duomenys pagal amziu
plt.figure(figsize=(16, 7))
plt.subplot(1, 2, 1)
sns.histplot(x='Age', hue='Survived', data=df, kde=True, palette='Set1', bins=30)
plt.title('Survival Distribution by Age (Actual)')
plt.xlabel('Age')
plt.ylabel('Count')
 
# Nuspejami duomenys pagal amziu
plt.subplot(1, 2, 2)
df_pred = pd.DataFrame({'Age': x_test['Age'], 'Survived': y_pred_log})
sns.histplot(x='Age', hue='Survived', data=df_pred, kde=True, palette='Set2', bins=30)
plt.title('Predicted Survival Distribution by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

print("----------------------------------")