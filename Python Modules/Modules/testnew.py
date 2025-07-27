



from  module import dishes

x = ("Cricket","Hockey","Football")

y = "Sports"

newdict = dict.fromkeys(x,y)


for x in newdict:
    if "Tennis" in x:
        print(f"Tennis is not present in {x} ")
    elif isinstance(x,bool) and x is None:
        print(f"{x} cannot be None or Booelan as per requirment")
    else:
        print(f"Remaining ones are {x}")


print(newdict)


from module import printHelloWorld

z = printHelloWorld("Mumbai")
print(z)



import re 

text = "Ayush 12 is a world"

res = re.findall("\Ayush",text)

print(res)




try:
    z = 1
    y = 0

    test = z/y

    if y == 0 and not type(y) == int:
        raise ZeroDivisionError(f"{y} cannot be zero and must be a valid numeric type")
    
except ZeroDivisionError as ze:
     print(f"{ze} Please check the value of {y}")

else:
    print(f"Result is : {test}")



from numbers import Number

try:
    a = 12

    b = 11

    sum = a + b

    if not (isinstance(a,Number) and isinstance(b,Number)): 
        raise TypeError(f"{a} and {b} must be valid integers")

    else:
        print(f"Sum of {a} and {b} is: {sum:.3f}")

except TypeError as te:
     print(f"{te} Either of {a} and {b} are not valid integers")



try:

    list1 = ["Ayush","World",12,False]

    list1.insert(3,"Worldish")

    if list1[1] not in list1:
        raise Exception("Item or element doesnt exist in the list")
    
    else:
        print(f"Value of 2 th element is: {list1[1]}")


except IndexError as ie:
     print(f"{ie} Please Check the value of that index and reenter a new value")


import random
try:
 
    randomNumber = str(random.randint(10**9, 10**10 - 1))
    countryCode = "+91"
    randomPhoneNumber = countryCode + "-" + randomNumber

    isStarts = randomPhoneNumber.startswith("+91")

    if not (isinstance(randomPhoneNumber,(str)) and isStarts and len(randomNumber) == 10):
       raise Exception(f"{randomPhoneNumber} must start with {countryCode} and {randomNumber} must be equal to 10")

    else:
        print(f"Random Indian Mobile Number is {randomPhoneNumber}")

    
except TypeError as ve:
       print(f"{ve} Please Check the random number must be a valid string type")



