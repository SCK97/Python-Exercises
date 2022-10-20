"""temperature = 20
if(temperature > 30):
        print("too hot")
        print("aagh")
        if(temperature > 50):
            print("AAH")
print("too cold")"""

#if temp is 40, will output too hot, aagh, too cold
#if temp is 60, will output too hot, aagh, AAH, too cold
#if temp is 20, will output too cold

#nested if statement means outputs overlap
#too cold prints as default as it's not within a statement
#can be fixed with elif statements


"""temperature = -10
if(temperature > 30):
        print("too hot")
        print("aagh")
if(temperature < 0):
    print("too cold")
if(temperature > 0):
    print("perfect")"""

#if temp is 20, will output perfect
#if temp is 60, will output too hot, aagh, perfect
#if temp is -10, will output too cold


"""temperature = 40
if(temperature > 30):
        print("too hot")
        print("aagh")
if(temperature < 0):
    print("too cold")
else(temperature > 0):
    print("perfect")"""

#in any situation that doesn't fit the conditions, will output perfect


temperature = 40
if(temperature > 30):
        print("too hot")
        print("aagh")
elif(temperature < 0):
    print("too cold")
else(temperature > 0):
    print("perfect")

#elif is more efficiant as only one condition can be true 
#it is not possible for it to be <0 and >30 simultaneously
#using else sets a defualt output of temps that don't meet the conditions