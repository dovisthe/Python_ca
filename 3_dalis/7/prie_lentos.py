import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
 
df = pd.read_csv('C:\\Python_ca\\3_dalis\\7\\train.csv')
dt = pd.read_csv('C:\\Python_ca\\3_dalis\\7\\test.csv')
gs = pd.read_csv('C:\\Python_ca\\3_dalis\\7\\gender_submission.csv')

#Train.csv Sutvarkome viska---------------------------------------------
df['FamilySize'] = df['Parch'] + df['SibSp']

df = df.drop(['Cabin', 'Ticket', 'Name', 'Parch', 'SibSp'], axis=1)

df['Age'].fillna(df['Age'].mean(), inplace=True)


Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1   
upperFilter = (df['Fare'] >= Q3 + 1.5 * IQR)
df.loc[upperFilter,['Fare']]  = Q3 + 1.5 * IQR

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

label_encoders = {}
for column in ['Sex']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

#Test.csv tvarkome--------------------------------------------------------------------

dt['FamilySize'] = dt['Parch'] + dt['SibSp']

dt = dt.drop(['Cabin', 'Ticket', 'Name', 'Parch', 'SibSp'], axis=1)

dt['Age'].fillna(dt['Age'].mean(), inplace=True)

 
Q1 = dt['Fare'].quantile(0.25)
Q3 = dt['Fare'].quantile(0.75)
IQR = Q3 - Q1   
upperFilter = (dt['Fare'] >= Q3 + 1.5 * IQR)
dt.loc[upperFilter,['Fare']]  = Q3 + 1.5 * IQR
dt['Fare'].fillna(dt['Fare'].mean(), inplace=True)

dt['Embarked'].fillna(dt['Embarked'].mode()[0], inplace=True)

label_encoders = {}
for column in ['Sex']:
    le = LabelEncoder()
    dt[column] = le.fit_transform(dt[column])
    label_encoders[column] = le

dt = pd.get_dummies(dt, columns=['Embarked'], drop_first=True)

#ML darome ---------------------------------------------------------------

x_train = df.drop('Survived', axis=1)
y_train = df['Survived']

x_test = dt
y_test = gs['Survived']

#Skaityme standartizavimo duomenis----------------------------------------
scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)


model = KNeighborsClassifier()
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)
print(classification_report(y_test, y_pred))
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)

#Heatmapas---------------------------------------------------

plt.figure(figsize=(10, 7))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()

















# Jei skirtusi mena amzius, reiketu pagal lyti uzpildyti tuscias vietas amziaus
# lyt = df.groupby('Sex')['Age'].mean()
# print(lyt)




# Įsiaiškinti kiek reikšmių yra tuščios ir kuriame stulpelyje +
# Kiek unikalių reikšmių turi kiekvienas stulpelis +
# Ar yra outliers +
# Koks duomenų pasiskirstymas. +
# Ar yra stulpelių kuriuos reikės išmesti. +
# Kurie duomenys yra svarbūs Survival ? (Koreliacija) +
# Ar duomenys nėra išbalansuoti ?  +
# Ar čia reikalinga panaudoti one-hot encoding ? +




# model = RandomForestClassifier()
# model.fit(x_train_scaled, y_train)

# y_pred = model.predict(x_test_scaled)
# print(classification_report(y_test, y_pred))
# print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# conf_mat = confusion_matrix(y_test, y_pred)
# print(conf_mat)






# print(df.head())
# print(df.info()) 


# print(df.info())
# print(df.isnull().mean())
# print(df.nunique())


# fare_survived_corr = df['FamilySize'].corr(df['Survived']) 
# print(fare_survived_corr)
 

# df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)


# sns.histplot(df['Age'])
# plt.show()


# print(df.head(60))
# print(df.describe())
# print(df.info())
# print(df.isnull().mean())
 
# print(df.nunique())
# sns.boxplot(df['Fare'])
# plt.show()
 
# sns.histplot(df['Fare'])
# plt.show()
 
