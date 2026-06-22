# Creating a list
numbers = [10, 20, 30, 40, 20]
print("List:", numbers)

# len()
print("Length of list:", len(numbers))

# max() 
print("maximum value:", max(numbers))

# min()
print("Minimum value:", min(numbers))

# sum() 
print("Sum of elements:", sum(numbers))

# append()
numbers.append(50)
print("After append(50):", numbers)

# count() 
print("Count of 20:", numbers.count(20))

# insert()
numbers.insert(2, 25)
print("After insert(25 at index 2):", numbers)

# extend()
numbers.extend([60, 70])
print("After extend([60, 70]):", numbers)

# pop() 
numbers.pop(3)
print("After pop(index 3):", numbers)

# remove() 
numbers.remove(20)
print("after remove(20)=", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse=", numbers)

