import numpy as np

data = np.array([10,22,22,66,44,8,55,44])


print(f"Data: \n{data}")

print(data)

mean = np.mean(data)
print(f"Mean: {mean}")

median = np.median(data)
print(f"Median: {median}")

std = np.std(data)
print(f"Standart deviation: {std}")

max = np.max(data)
print(f"Max: {max}")

min = np.min(data)
print(f"Min: {min}")

print()
print("--------------------------------------------")
print()


data1 = np.array([[1,2,3],[4,5,6]])
data2 = np.array([[4,5,6],[4,5,6]])

print(f"Data 1: \n{data1}")
print(f"Data 2: \n{data2}")

sum_data = data1 + data2
print(f"Sum of matrix: {sum_data}")

multiplication_data = data1 * data2
print(f"multiplication of matrix: {multiplication_data}")

print()
print("--------------------------------------------")
print()

print(f"Data: \n{data}")

filtered_data = data[data > 30]

print(f" Filtered data : \n{filtered_data}")

condition = ((data % 2 == 0) & (data > 30))

filtered_data_2 = data[condition]
print(f"FIltered data :  \n {filtered_data_2}")

print()
print("--------------------------------------------slice")
print()

data3 = np.array([10,22,22,66,44,8,55,44])


print(f"Data3: \n{data3}")

# array[start:stop:step]

slice_data3 = data3[::2]
print(f"slice Data4: \n{slice_data3}")




data4 = np.array([[1,2,3],[4,5,6],[7,8,9],[4,5,6],[7,8,9]])

print(f"Data4: \n{data4}")
#             eilute            stulpelis
# array[start:stop:step, start:stop:step]


data4[2,0] = 20

slice_data4 = data4[:, :1]
print(f"slice Data4: \n{slice_data4}")

value_data4 = data4[0,2]
print(f"Valute data 4: \n{value_data4}")


print()
print("--------------------------------------------random")
print()

data5 = np.random.randint(-50,51, (15,15))

print(f"Random data5: \n{data5}")

data6 = np.random.normal(5, 1, (15,15))
data6 = np.round(data6). astype(int)

print(f"Random data5: \n{data6}")

print()
print("--------------------------------------------random")
print()

data7 = np.array([[1,2,3]])
data8 = np.array([[4,5,6]])

print(f"Random data7: \n{data7}")
print(f"Random data8: \n{data8}")

data_vertical = np.vstack((data7,data8))
data_vertical = np.vstack((data_vertical,data8))

print(f"Vertical vertical: \n{data_vertical}")


data_horizonta = np.hstack((data7,data8))
data_horizonta = np.hstack((data_horizonta,data8))

print(f"Horizontal : \n{data_horizonta}")