#https://www.w3resource.com/python-exercises/string/
#2. Write a Python program to count the number of characters (character frequency) in a string.
    #Sample String : google.com'
    #Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

s = input("Please enter some text: ")

results = dict()

for i in s:
    if i in results:
        results[i] = results[i] + 1
    else:
        results[i] = 1

print("Character count: ")
print(results)