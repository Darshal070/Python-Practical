import pandas as pd
import numpy as np

# 1. Create Series from Array
arr = np.array([10, 20, 30, 40])
series_from_array = pd.Series(arr)

print("Series from Array:")
print(series_from_array)


# 2. Create Series from List
lst = [5, 15, 25, 35]
series_from_list = pd.Series(lst)

print("\nSeries from List:")
print(series_from_list)


# 3. Access Elements of Series
print("\nAccessing Elements:")
print("First element:", series_from_list[0])
print("Last element:", series_from_list[3])


# 4. Create DataFrame using Dictionary
data = {
    "Name": ["Amit", "Rahul", "Sneha"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame from Dictionary:")
print(df)


# (Optional) DataFrame from List
data_list = [
    ["Amit", 21, 85],
    ["Rahul", 22, 90],
    ["Sneha", 20, 88]
]

df2 = pd.DataFrame(data_list, columns=["Name", "Age", "Marks"])

print("\nDataFrame from List:")
print(df2)
