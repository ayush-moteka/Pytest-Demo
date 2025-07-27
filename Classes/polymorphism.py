

#Polymorphism --> IF we want to execute same methods for different class names then we use this feature



class Principal:
      
      def __init__(self,exp,age):
            self.exp = exp
            self.age = age

      def printHello(self):
            print("Hey")


class Teacher:
      
      def __init__(self,exp,age):
            self.exp = exp
            self.age = age

      def printHello(self):
            print("Hello")


class SportsTeacher:
      
      def __init__(self,exp,age):
            self.exp = exp
            self.age = age

      def printHello(self):
            print("Sports world")



x = Principal("Forty three",25)
y = Teacher("Forty",35)
z = SportsTeacher("Forty one",45)


for res in (x,y,z):
      print(res,"res")
      print(res.exp)
      print(res.age)
      res.printHello()





#Using Inheritance for child and Parent class


class Parent:
      
      def __init__(self,salary,food):
            self.salary = salary
            self.food = food
            self.passion = "Cricket"

    
      def printMessage(self):
            return f"My favourite food is {self.food} and salary is {self.salary:.2f} and my passion is {self.passion}"
 
    

class Child(Parent):
      pass

class SubChild(Parent):
      
      def printMessage(self):
            return "Hey People"


class GrandChild(Parent):
      """
       def printMessage(self):
            return "World is good"
      """
     
      def printMessage(self):  #This print message method is inherited from parent class using super keyword
            return super().printMessage()

ch = Child(23.23,"French fries")
sub = SubChild(123.45,"Paneer Tikka")
grandchild = GrandChild(1203,"Noodles")


for result in (ch,sub,grandchild):
      print(result.food)
      print(result.salary)
      print(result.passion)
      print(result.printMessage())
    






      


