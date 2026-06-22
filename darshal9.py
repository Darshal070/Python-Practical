#Creating a tuple
t = (10, 20, 30, 40, 50)
print("Tuple:", t)

#Accessing tuple elements
print("First element:", t[0])
print("Last element:", t[-1])
print("elements 1 to 3:", t[1:4])

#Updating tuple
tup= list(t)
tup[2] = 35
t = tuple(tup)
print("tuple:", t)

#Deleting tuple
tup = list(t)
del tup[1]
t = tuple(tup)
print("element:", t)

# Deleting tuple
del t
print("tuple deleted")

#converting tuple to list
t2 = (1, 2, 3, 4)
lst = list(t2)
print("Tuple:", t2)
print("Converted List:", lst)
