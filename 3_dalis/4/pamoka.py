import seaborn as sns
import matplotlib.pyplot as plt


# data = [4,9,1,4,5]

# sns.lineplot(data)
# plt.title("vienasdutryketruipenki? kas dabar bus")
# plt.xticks(range(0,5))
# plt.show()


# names = ["Justas","Karolis","Mantas"]

# counts = [41,58,5]

# sns.lineplot(y=counts, x=names)

# plt.show()

names = ["Justas","Karolis","Mantas"]

counts = [41,58,5]

sns.barplot(y=counts, x=names)

plt.show()