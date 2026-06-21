#continue
for var in"MSBTE":
    if var==10:
        continue
    print(var)

#pass
    n=10
    if n>10:
        pass
    print('Hello')

#break
    letter=input("enter a letter:")
    
    if letter=='e' or letter=='s':
        break
print('current Letter:',letter)

#nested if-else

num = int(input("Enter a number: "))

if num >= 0: 
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
else: 
    if num % 2 == 0:
        print("The number is Even (Negative)")
    else:
        print("The number is Odd (Negative)")
