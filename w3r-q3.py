#https://www.w3resource.com/python-exercises/string/
#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
    #If the string length is less than 2, return instead of the empty string.
        #Sample String : 'w3resource'   Expected Result : 'w3ce'
        #Sample String : 'w3'           Expected Result : 'w3w3'
        #Sample String : ' w'           Expected Result : Empty String

s = input("Please enter some text: ")
result = ""

if len(s) >= 2:
    result = s[0] + s[1] + s[len(s)-2] + s[len(s)-1]
    print(result)
else:
    print(result)