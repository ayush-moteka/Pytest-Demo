

#Inheritance allows us to access all the properties and methods of one class in another class

#Child class derives the properties and methods from parent class

# Child class is also called as base class

# Parent class is also called as derived class



class ParentClass():
 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printNameAge(self):
        return f"My name is {self.name} and age is {self.age}"
    
parent = ParentClass("Ayush",25)

print(parent.printNameAge())



class childClass(ParentClass):
      pass

child = childClass("Ayush",24)


print(child.printNameAge())


# 2 ways to add New properties 

1. #By passing it without a paramter 
class newChildClass(ParentClass):
     
     def __init__(self, name, age):
          super().__init__(name, age)
          self.country = "India"

     
ch = newChildClass("World",21)
print(ch.country)


2. #By passing through a paramter 

class newtestClass(ParentClass):
     
     def __init__(self, name, age,country):
          super().__init__(name, age)
          self.country = country

     def printCountry(self):
          return f"Country name is :{self.country}"
     
     def printNameAge(self):
          return super().printNameAge()
     

resultobject = newtestClass("Ayush",21,"New Zealand")

print(resultobject.printCountry())
print(resultobject.printNameAge())


#Add Methods to child class 


class newchildtestClass(ParentClass):
     
     def __init__(self, name, age):
          super().__init__(name, age)
          self.bookName = "Marcus Intentions"

     
     def printBookName(self):
          return f"The book name is {self.bookName.replace("c","n")}"


book = newchildtestClass("Ayush",23)

print(book.printBookName())



class Cricket:
     
     def __init__(self,format,channel):
          self.currentformat = format
          self.boradcastchannel = channel
          self.passion = "cricket"
     def printCricketData(self):
          print(f"My passion is {self.passion}favourite format in cricket is {self.currentformat} and where i watch is in {self.boradcastchannel}")
     
   
     def printMyPassion(self):
          print("After this will call the print Cricket data function")
          self.printCricketData() #Called the printCricketdatamethod
          



class Hockey(Cricket):
     
     def __init__(self, format, channel):
          super().__init__(format, channel)
          self.hockeylegacy = "SardarSingh"
          
     def printMyPassion(self):
          print(f"Currently I like Hockey also and my fav player is: {self.hockeylegacy.strip().capitalize()}")
          return super().printMyPassion()
     

hoc = Hockey("T20Format","SonySports")
hoc.printMyPassion()





