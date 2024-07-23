import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#Užduotis: Naudodami Seaborn, sukurkite daugiafunkcinį grafiką,
# kuriame būtų linijinė grafika, barplot grafikas ir histograma

x = np.arange(0, 21)
y = 2 * x + 3

#Linijinis grafikas------------------
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Barplot grafikas-------------------
items = ['Prekė A', 'Prekė B', 'Prekė C', 'Prekė D', 'Prekė E']
sales = np.random.randint(10, 100, size=len(items))

sns.barplot(x = items, y = sales)
plt.xlabel('Prekes')
plt.ylabel('Kaina?')
plt.show()

# Histogramos grafikas-----------------------

data = np.random.randint(0, 100, size=50)

sns.histplot(data, bins=50, kde=False)
plt.xlabel('X')
plt.ylabel('Kaip daznai?')
plt.show()

