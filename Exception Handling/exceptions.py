



#Exception Handling --> It is a mechanism used by the developer to handle differennt exceptions 


#Ex: 1 

try:
    print(x,"x")
except NameError:
    print("X is not defined , Please define or assign value to x")
else:
     print(f"Value of x is:{x}")
finally:
    print("THis code will get executed irrespective whether the try or catch has executed or not ")


#Ex:2
try:
    x = 24
    if not (isinstance(x,int) and x % 2 == 1 and  x > 0): raise ValueError(f"{x} is not an even number")
except:
     print(f"{x} must be greater than 0 and a valid integer and an even number")
else:
    y = 34
    sum = x + y
    print(sum,"summ")
    print("No problem code is without an exception")


#Ex:3

try:
    x = 21
    x = int(x)
    test = 1/(x % 2 == 0) #Zero division error
    print(x)
except ZeroDivisionError:
    print(f"{x} is an even number please enter an odd number")
else:
    print("No exception has occured...")
finally:
    print("Will by default get executed....")



#Ex:4 - Import error which is an predefined exception

try:
    import ress
    str = "Hello Ayush how are u?"
    isSearch = ress.search("\d",str)
    print(isSearch)
except ImportError:
    print("There is an import error please import the module correctly ")
else:
    print("No exception occured")


#Ex:5 

try:
    import random
    
    randonnumber = random.randint(100000000,9999999999)
    countryCode = "+91"
    randomIndiaPhoneNumber = countryCode + "-" + str(randonnumber)
    splittedNumber = randomIndiaPhoneNumber.split('-')
    assert len(splittedNumber[1]) == 10 and randomIndiaPhoneNumber.startswith("+91")
    print(f"My current Indian mobile number is:{randomIndiaPhoneNumber}")

except ImportError as ie:
    print(f"{ie}")


    

try:
    index = 2
    list1 = ["Ayush","World"]
   
    
    list2 = list1.copy()
    list2.insert(2,"Brendon")
    
    print(list2[index])

except IndexError as ierror:
      print(f"{ierror} There is no elemnent that exists in the list with that index:{index}")

else:
    print("No exception has occured..")


#Ex:6

try:
    x = "World"
    if type(x) == "str":  
      print(f"This {x.upper()} is of type string ")

except IndentationError:
    print("There is indendation error ")

else:
    print("There is no error..")



#Ex:7 --> Type error 

try:
    num1 = 23
    num2 = 3.23
    if not(isinstance(num1,int) and isinstance(num2,int) and num1 > 0):
        raise TypeError("Only integers are allowed")
    else:
        sum = num1 + num2
        print(sum,"sum of num1 and num2")
except:
    print(f"{num1} and {num2} must be intergers")

else:
    print("No exception occured")


    

#Ex: 8 Without try and except throw customised exceptions using raise keyword


x = 21
y = 3

if not isinstance(x,int): raise Exception("x is not an valid integer, Please Enter a valid integer")

if not isinstance(y,int):  raise Exception("y is not an valid integer, Please Enter a valid integer")

else: print(f"{x} and {y} are both valid integers ")




#Ex: Zero division error


try:
    a = 10
    b = 0

    if b == 0 and a / b == 0:
        raise ZeroDivisionError("b is zero and a number cant be divided by zero")
    
except ZeroDivisionError as zero:
       print(f"{zero} , Please Enter a Number which is greater than zero")

else:
    print(f"Division of {a} and {b} is {a / b:.2f}")




