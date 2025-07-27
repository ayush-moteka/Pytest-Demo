


#Sum of 2 numbers only for integer types 
def sum(a,b): #Parameters -->these are given during function definition
    if isinstance(a,int) and isinstance(b,int):
        print(f"Sum of a nd b is {a + b}")
    else:
        print(f"{a} and {b} paramters are not passed correctly with type integers , Please enter a valid integer")
        

sum(21.23,1) #Arguments --> these are passed during calling a function

#Checking if passed arguments are accepted for all types of Numeric data types
import numbers #or from numbers import Number

def allNumericTypes(x,y):
    if isinstance(x,numbers.Number) and isinstance(y,numbers.Number):
        print(f"Sum of both numbers are: {x + y}")
    else:
        print("Please enter a valid Numeric type")

allNumericTypes(21,23)



def namesData(fname,lname):
    fullname = fname + " " +  lname
    print(f"My first name is {fname} and last name is {lname} and fullname is {fullname.title().strip()}")
    return fullname


namesData("ayush","moteka")



from numbers import Number
def printAverageofthreeNums(e,r,t):
    if isinstance(e,Number) and isinstance(r,Number) and isinstance(t,Number):
        print(f"{e}{r}{t} are valid numbers")
        sumofthreeNums = e + r + t
        average = sumofthreeNums / 3
        return average
    else:
        print(f"Either of {e}{r}{t} are not valid numeric types")


printAverageofthreeNums(11,34,5)





#If we are not sure about the arguments we are going to pass then we can use Arbitary arguments (*args)
def argsDemo(*args):
    print(args,"args")
    average = (args[0] + args[1] + args[2]) / 3
    print(average,"average")
    return average

#args = (21,34,87) --> Tuple 
argsDemo(21,34,87)


def calculatelbhRectangle(*args):
    
    areaofRectangle = args[0] * args[1] * args[3]

    return areaofRectangle

print(calculatelbhRectangle(21,34,5,34))


#Keyword Arguments (key = value) Syntax -- here the order of the arguments doesnt matter


def keyValue(x,y,z):
    if x % 2 == 0 and y % 2 == 1 and z > 2:
        print(f"{x} is an even number and {y} is an odd number and z is greater than 2")
    elif isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        print(f"{x} {y} {z} are all integer data types")
    else:
         print("Test..............")

    return True

keyValue(y=2,x=1,z=44) 


def printIncomeTax(price,tax):

    if isinstance(price,int) and isinstance(tax,int):
        regularTax = (price * tax) / tax
        print(f"Price is :{"More" if regularTax > 10 else "Cheap"}")
        return regularTax

printIncomeTax(tax = 12,price = 12000)

#Arbitary Key arguments often named as **kwargs and passed as dictionary (key:value)

def kwardsDemo(**args):
    print(args,"args")
    fullname = args["firstname"] + " " + args["lastName"]
    print(f"Hello my name is {args["firstname"]} and {args["lastName"]} and fullname is {fullname.title()}")
    return args
#args = {"firstname":"ayush","lastName":"moteka"} --> Dictionary
kwardsDemo(firstname = "ayush",lastName = "moteka")



#Default Parameter Value -- We pass the default paramter here and that value is taken when we call the function and if new value is called then it will over ride the default value


def defaultParams(name = "Rajesh"):
    isStarted = name.startswith("R")
    newName = name.replace("j","m")
    if isStarted == True and len(newName) > 2: print(f"The updated name is {newName}")
    else: print(f"{name} doesnt start with R and cant be considered")

defaultParams()
defaultParams("India")



#Pass a list as an argument

listofSchools = ["Timpany","SriPrakash","Wonderla","Tinythoughts"]

def ListDemo(school):
    
    for x in school:
        print(f"{x} is my childhood school") if x == "SriPrakash" else  print(f"This is my favorite school :{x}") if x == "Timpany" else print(f"These are other remaining schools: {x}")


ListDemo(listofSchools)

#Pass -- If we want a function with no content and empty data then we can use pass to avoid getting an error

def passDemo():
    pass

passDemo()

#Postional - Only Arguments --> Normal arguments passed without keywords and are denoted by ,/

def positionalDemo(x,/):
    print(x,"X")


#positionalDemo(x = "Ayush") #This will throw an error saying it will only accept positional args , not keyword args
positionalDemo("Ayush")



#Keyword - Only Arguments  --> Only keyword based arguments are allowed, positional are not allowed --> add an *, before the first paramter


def keywordDemo(*,x):
    print(x,"newww")

#keywordDemo(5)#This will throw an error saying it will only accept keyword args , not positional args
keywordDemo(x = "World")



#Combining both postional only and keyword only args


def combineArgs(a,b,/,*,r,t):
    sum = a + b
    print(sum,"summ")
    z = r + " "  + t
    print(z,"zz")
    
combineArgs(10,23,r = "Rate",t = "trip")



def newtest(*args):
    print(type(args))
    areaofRectangle = args[1] * args[0] * args[2]
    
    return areaofRectangle


print(newtest(1,3,5))


def new(u,v):
    
    world = u
    hello = v
    
    return hello + " " + world

print(new(u="Brendon",v="Mccullum"))


def keyargsdemo(**kwargs):
    assert type(kwargs) == dict
    series = kwargs["test"] + "" + kwargs["present"] 
    
    print(series)
    

keyargsdemo(test = "Currentone",present = "Latest")


def defaultargsdemo(username = "AyushMoteka",password = "ayush@#123"):
    
    logincredentials = {
        "username":username,
        "password":password,
        "email":"ayush@#123"
    }

    for x in logincredentials:
        if x == "email":
            print(f"My current email is:{logincredentials[x]}") 
        else:
            print(f"Remaining keys of the dict are :{x} and its values are {logincredentials[x]}")
            

defaultargsdemo(username = "BrendonMcullum") #This will override the username paramter during the function definition


def poskeycheck(a,b,/,*,c,d,e):
    
    average = (a + b + c + d)/e
    
    rounded = f"{average:.3f}"
    
    return rounded

print(poskeycheck(2,3,e=1,c=4,d=5))





