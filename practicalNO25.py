import pandas as pd
import numpy as np

# 1. Series from array
print("1. Series from array")
arr = np.array([10, 20, 30])
print(pd.Series(arr))

# 2. Series from list
print("\n2. Series from list")
print(pd.Series([85, 90, 78]))

# 3. Access elements
print("\n3. Access elements")
s = pd.Series([100, 200, 300])
print("First:", s[0])

# 4. DataFrame
print("\n4. DataFrame")
data = {"Name": ["Darshal", "Amit"], "Marks": [88, 92]}
print(pd.DataFrame(data))
