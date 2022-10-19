number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if number1 > number2:
    number1bigger = True
else:
    number1bigger = False

print("It is ",number1bigger,"that number1 is bigger")

#the if else statement is comparing number1 to number2
#if number 1 is bigger, then it creates the number1bigger variable and assignes it the boolean value "True"
#if this is not the case, number1 is equal to or smaller than number2 so number1bigger is assigned "False"