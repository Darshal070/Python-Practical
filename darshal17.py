# Import required modules
import math
import random
import os

# 1. Math Module
print("=== Math Module Example ===")
num = 16

print("Square root of", num, "is:", math.sqrt(num))
print("Value of pi:", math.pi)
print("Power (2^3):", math.pow(2, 3))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))


# 2. Random Module
print("\n=== Random Module Example ===")

print("Random number between 0 and 1:", random.random())
print("Random integer between 1 and 10:", random.randint(1, 10))

list1 = [10, 20, 30, 40, 50]
print("Random choice from list:", random.choice(list1))

random.shuffle(list1)
print("Shuffled list:", list1)


# 3. OS Module
print("\n=== OS Module Example ===")

print("Current working directory:", os.getcwd())

print("List of files and directories:")
print(os.listdir())

# Create a new directory
os.mkdir("test_folder")
print("Directory 'test_folder' created")

# Rename the directory
os.rename("test_folder", "new_folder")
print("Directory renamed to 'new_folder'")

# Remove the directory
os.rmdir("new_folder")
print("Directory 'new_folder' removed")
