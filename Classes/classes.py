
# A class IS A object constructor or a blueprint that has property and methods

class MyClass :
     x = 10  #Property of the class

    
res = MyClass()
print(res.x,"p")


#Once the class is initiated there is a built in function init function that is called
#Use the init function to assign values to properties  

class NewClass() :
     
     def __init__(self,name,age):  #Self parameter is used to access the variables inside the class.
        self.name = name
        self.age = age

z = NewClass("Ayush",23)
# z object will have access to all the properties and methods of the class 
print(z.name)
print(z.age)
print(z)



#There is built in _str_ function to make sure the string representation of the object

class stringfuncDemo:
    
    def __init__(self,name,age):
       self.name = name
       self.age = age


    def __str__(self):
        if isinstance(self.age,int) and self.age != 0:
          return f"My name is {self.name} and age is ({self.age:.2f})"


y = stringfuncDemo("Rohan",23)        
print(y)



#Object Methods --> A class or an object constructor can have methods also.


class objectMethodsDemo :
    
    def __init__(self,name,city,age):
        self.name = name
        self.city = city
        self.age = age

     
    def customFunc(self):
         return f"My name is {self.name.title()} and i belong to city of Dreams {self.city.capitalize()} and my age is {self.age:.1f} years old"



res = objectMethodsDemo("Ayush","Mumbai",25)
print(res.customFunc())



#Self parameter --> It is used to refer to the current instance of the class and used to refer or access the variables of that class
# It must not be self , it can be any name but it must be the first parameter of that function

#Example without self paramter:


class selfDemo :
    
    def __init__(test,book,country):
        test.book = book
        test.country = country

     
    def custfunc(x):
        return f"My favourite book is {x.book} and country is {x.country.upper()}"
    

obj = selfDemo("Test of the Best","us")
obj.country = "Singapore"

print(obj.custfunc())
print(obj.book)
print(obj.country)

   

#Modify Object Properties

obj.book = "Hello World"
obj.country = "Middle West"

print(obj.book,"updated book")
print(obj.country,"updated country")


#Delete object properties

del obj.book

#print(obj.book)


#Delete object

del obj

#print(obj)


#Pass keyword -- class with no content and empty data and not to get an error from python


class testPass:
    pass




