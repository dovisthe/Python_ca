import numpy as np

data = np.array([10,22,22,66,44,8,55,44])


print(f"Data: \n{data}")

mean = np.mean(data)
print(f"Mean: {mean}")

median = np.median(data)
print(f"Median: {median}")

std = np.std(data)
print(f"Standart Deviation: {std}")

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

sum_data =  data1 + data2
print(f"Sum of matrix: \n{sum_data}")

multiplication_data =  data1 * data2
print(f"Multiplication of matrix: \n{multiplication_data}")

print()
print("--------------------------------------------")
print()

print(f"Data: \n{data}")

filtered_data = data[data > 30]
print(f"Filtered data: \n{filtered_data}")

condition = ((data % 2 == 0) & (data > 30))

filtered_data_2 = data[condition]
print(f"Filtered data 2: \n{filtered_data_2}")


print()
print("-------------------------------------------- Slice")
print()
#Slice

data3 = np.array([10,22,22,66,44,8,55,44])

print(f"Data 3: \n{data3}")

# array[start:stop:step]

slice_data3 = data3[::2]
print(f"Slice Data 3: \n{slice_data3}")




data4 = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[4,5,6],[7,8,9]])

print(f"Data 4: \n{data4}")
#          eilutes         stulpelis
# array[start:stop:step, start:stop:step]
# array[start:stop,      start:stop]

data4[4, 0] = 20

slice_data4 = data4[:, :1]
print(f"Slice Data 4: \n{slice_data4}")

value_data4 = data4[0, 2]
print(f"Value Data 4: \n{value_data4}")

print()
print("-------------------------------------------- Random")
print()

data5 = np.random.randint(-50, 51, (15,15))

print(f"Value Data 5: \n{data5}")

data6 = np.random.normal(5, 1, (15,15))
data6 = np.round(data6).astype(int)

data_unique = np.random.choice(range(50), (2,2), False)
data_float_unique =  np.random.rand(5,5)
print(f"data_float_unique: \n{data_float_unique}")
print(f"data_unique: \n{data_unique}")
print(f"Value Data 6: \n{data6}")


print()
print("-------------------------------------------- Stack")
print()

data7 = np.array([[1,2,3]])
data8 = np.array([[4,5,6]])

print(f"Value Data 7: \n{data7}")
print(f"Value Data 8: \n{data8}")

data_vertical = np.vstack((data7, data8))
data_vertical = np.vstack((data_vertical, data8))

print(f"Value Data Vertical: \n{data_vertical}")

data_horizontal = np.hstack((data7, data8))
data_horizontal = np.hstack((data_horizontal, data8))

print(f"Value Data Horizontal: \n{data_horizontal}")


