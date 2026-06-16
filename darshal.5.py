#while loop
count = 0

while count < 5:
    print(count)
    count = count + 1

print("Good Bye")

#for loop
for letter in "python":
    print(letter)

fruits = ["banana", "apple", "mango"]

for fruit in fruits:
    print("Current fruit:", fruit)


#Nested loops
    i = 2

while i < 20:
    j = 2
    is_prime = True

    while j <= i // 2:
        if i % j == 0:
            is_prime = False
            break
        j = j + 1

    if is_prime:
        print(i)

    i = i + 1
