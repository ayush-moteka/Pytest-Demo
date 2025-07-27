
#Ex:1

print("Please Enter your name:")

name = input()
print(type(name))
print(f"My name is {name}")



#Ex:2 

names = input("Please Enter a name:")
city = input("Please Enter City Name:")
try:
   if not names and isinstance(names,str):
      raise Exception("Please Enter a name")
   if not city and isinstance(city,str):
      raise Exception("Please Enter City Name ")
   
except :
   print("Name and city are required as input from the user")


else:
    print(f"My name is {names.strip().title()} and I am from {city.strip().title()}")



#Ex: 3


import math
from numbers import Number
try:
     number = input("Please Enter a Number:")
     finalres = math.sqrt(float(number))
     if finalres == 0: 
          raise ValueError(" 0 is not a Valid Integer ")
     if not isinstance(finalres,Number):
        raise TypeError(f"{finalres} is not a valid Integer")
except (ValueError,TypeError) as ve:
      print(f"{ve} , Please Enter a Valid Number")

else: print(f"Square root of {number} is {finalres}")







