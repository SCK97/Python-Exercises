num = int(input("Please enter your mark: "))

if num > 90:
    grade = "Merit"
elif num > 80:
    grade = "Distinction"
elif num > 65:
    grade = "Pass"
else:
    grade = "Fail"

print(grade)