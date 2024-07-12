import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pardavimai = np.random.randint(50, 500, (366))
dates = pd.date_range(start='2024-01-01', end="2024-12-31")

sarasas = pd.Series(pardavimai, index=dates)
print("Original Series:")
print(sarasas)

print("-------------------------------")

sarasas[300] = 1000
sarasas[100] = 1500
sarasas[10] = -1300

weekly = sarasas.resample('W').mean()
weekly.index = weekly.index[:-1].append(pd.Index([pd.Timestamp("2024-12-31")]))
print("\nWeekly Mean Sales:")
print(weekly)

print("-------------------------------")

monthly = sarasas.resample("ME").mean()
print("\nMonthly Men Sales:")
print(monthly)

print("-------------------------------")


vidurkis = sarasas.mean()

std = sarasas.std()

threshold_minus = vidurkis - std * 2
threshold = vidurkis + std * 2


nukrypimas = sarasas[(sarasas > threshold) | (sarasas < threshold_minus)]
print(nukrypimas)




plt.figure(figsize=(10, 5))
plt.plot(sarasas.index, sarasas, label='Daily Sales')
plt.scatter(nukrypimas.index, nukrypimas, color='red', label='Outliers')
plt.axhline(y=vidurkis, color='g', linestyle='-', label='Mean')
plt.axhline(y=threshold, color='m', linestyle='--', label='Upper Threshold (Mean + 2*Std)')
plt.axhline(y=threshold_minus, color='m', linestyle='--', label='Lower Threshold (Mean - 2*Std)')
plt.title('Sales Data with Outliers Highlighted')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()