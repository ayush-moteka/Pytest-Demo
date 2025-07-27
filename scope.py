




#Scope defines accessibility of a variable

#Local Scope --> That variable can be accessed only within that particular function or method

#Even inside the main function if there is any other inner or nested function we can access it


def mainfunc():
    x = 500
    name = "  Ayush  "

    def innerfunc():
        print(x,"x")
        isStarts = name.strip().startswith("A")
        if isStarts: print(f"My name is {name.strip()}")
    innerfunc()


mainfunc()


#Use global keyword to access the variable from anywhere outside the function --> 
#If we dont give it as global we cant access the variable outside the function , it can only be accessed within that function
#Example: 1
z = 500

def func1():
    global z
    z = 300

func1()

print(z,"zz") #Output should be 300

#Example 2: Global keyword

list = ["Ayush","Tarun","Kumud"]

def listfunc():
    global list
    list = ["Ayush","Tarun"]
    list1 = ["Hirama","World"]
    list.extend(list1)
    return list

listfunc()


print(list,"list") #Output should be ayush,tarun, hirama, world as there is  global keyword 





#Non -Local keyword




def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
    


z = 5000
def Outerfunc():
   
   z = 1000

   print(z)

Outerfunc()

print(z)


#Using global keyword we can access the variable outside the function and anywhere we want

w = "whirpool"

def globalDemo():
   
   global w
   
   w = "testers"

   print(w)

globalDemo()

print(w)

#Inner demo

def outer():
   
   global xest
   xest = 1000

   def inner():
      print(xest)

   inner()
  
outer()

print(xest,"xest")



