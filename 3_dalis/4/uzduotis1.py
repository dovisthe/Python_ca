import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')
titanic = sns.load_dataset('titanic')

print("----------------------------------------")

# sns.countplot(x='class', data=titanic)
# plt.title("Keleivius skc pagal klase")
# plt.xlabel("klase")
# plt.ylabel("skaicius")

# plt.show()

print("----------------------------------------")

# sns.catplot(x='class', y='survived', hue='sex', data=titanic, kind='point')
# plt.show()

print("--------------------------")

# sns.violinplot(x='class', y='age', data=titanic)

# plt.title('amzius pagal klase')
# plt.xlabel('klase')
# plt.ylabel('amzius')

# plt.show()

print("----------------------------------------")

# sns.histplot(data=titanic, x='age', hue='survived', bins=20, multiple='stack')
# plt.title('survival by age')
# plt.xlabel('age')
# plt.ylabel('survived')
# plt.show()

print("----------------------------------------")

# sns.heatmap(titanic.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm')
# plt.title('Heatmap')
# plt.show()

print("----------------------------------------")

# sns.catplot(data = titanic, x='sex', y='age', hue='survived', kind='violin')
# plt.show()