


import module as mx #Giving Alias name to the module name

print(mx.printHelloWorld("Vizag"))

print(mx.dishes["cake"][0])


#Built in modules

import random

print(random.randrange(0,122))


import platform

allnames = dir(platform)
print(allnames)

import numbers
x = dir(numbers)  #dir function will give all the functions and variables inside the module which can be created by us or built in module also
print(x)

import module
y = dir(module)
print(y)

#If we want to only import only a part from a module means only a single function or singl variable or lists or any data type
# then we use the from keyword


from module import dishes  #Only import dishes dict from module 
from module import printHelloWorld #Only import this function from module
print(dishes.get("price"))
print(printHelloWorld("Vizag"))







