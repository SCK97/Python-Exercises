a = int(input("Please enter a number: "))
b = int(input("Please enter a second number: "))
c = int(input("Please enter a third number: "))

print("The largest number you entered is:")

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print (c)
