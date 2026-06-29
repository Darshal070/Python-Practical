import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

print("Student Data:")
print(df)

# Display first 2 rows
print("\nFirst 2 Records:")
print(df.head(2))

# Display last 2 rows
print("\nLast 2 Records:")
print(df.tail(2))

# Find maximum marks
print("\nMaximum Marks:", df["Marks"].max())

# Find average marks
print("Average Marks:", df["Marks"].mean())

# Filter students with marks > 80
print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])
