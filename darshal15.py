from functools import reduce

# 1. Lambda function
square = lambda x: x * x
print("Lambda Function :")
print("Square of 5 is:", square(5))


# 2. Map function
numbers = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x * x, numbers))

print("Map Function :")
print("Original list:", numbers)
print("Squared list:", squared_list)


# 3. Reduce function
product = reduce(lambda x, y: x * y, numbers)
print("Reduce Function :")
print("Original list:", numbers)
print("Product of all elements:", product)
