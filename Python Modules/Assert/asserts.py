

weather = "Rainy"
message = "Happy Weekends"  

match weather:
    case "Sunny" | "Winter" | "Thunderstroms":
        print(f"Current weather is of:{weather}")
    case "Rainy" if message == "Happy Weekend" and not len(message) == 0:
        print(f"Current weather is my favourite and it is{weather}")
        message = "Have a rainy day"
    case _:
        print("None of the above..")

print(message)

x = "Ayush is a Cricketer" 

y = 2034


assert type(x) == str and type(y) == int,"The x and y variables are of not valid data type"


list1 = ["World","Trip","Not","Avaiable",False]

assert isinstance(list1,list) and isinstance(list1[4],bool)


set1 = {"agent","Microsoft","Industry"}

assert "agent" in set1 or "ayush" not in set1


tuple1 = ("name","city","test")

assert type(list(tuple1)) == list


x = 23

y = 10

print(f"x / y: is ")

assert y != 0,"Zero division error"



def calculaterectangleArea(l,b):

    assert l > 0 and b > 0, "Length and breadth must be greater than zero"

    area = l * b

    return area
    

finalarea = calculaterectangleArea(10,21)

print(finalarea)


listofNums  = [211,100,130,213]

failed  = 16
for x in listofNums:
    assert x >= 16,"Less than 16 is considered as failed"
    print(f"The considered marks as passed are: {str(x)} Pass ")

sumofnums = sum(listofNums)
assert sumofnums > 0 and not sumofnums == 0,"Sum cannot be zero and must be greater than zero"
print(sumofnums,"summ")



class myBook:
      
      def __init__(self,title):
           self.title = title
           self.book = "World is not a place"
      
      def __str__(self):
           return self.title.title()
        
      def getBookTitle(self):
           isStarts = self.book.startswith("W")
           if isStarts and self.book != "English men":
            return self.book
           
resultobj = myBook("Wow Harry Potter")
 

print(resultobj.getBookTitle(),"res")









def calaculateAreaRec(**kwargs):
    
    assert type(kwargs) == dict and kwargs["length"] > 0 and kwargs["breadth"] and kwargs["height"] > 0 , "keyword arbitary arguments must be of type dict and value mus tbe greater than 0"
     
    totalArea = (kwargs["length"] * kwargs["breadth"] * kwargs["height"]) / 3

    return totalArea #kwargs = {lenght:5,breadth:5,height : 6}


print(calaculateAreaRec(length = 5 , breadth = 5, height = 6))


def calaculateAreaRec1(*args):
    
    assert type(args) == tuple and args[0] > 0 and args[1] and args[2] > 0 , "arbitary arguments must be of type tuple and value mus tbe greater than 0"
     
    totalArea = (args[0] * args[1]  * args[2]) / 3

    return totalArea


print(calaculateAreaRec1(21,34,56)) #args = (21,34,56)





def calaculateAreaRec2(l,b,h):
    
    assert type(l) == int and l > 0 and b > 0 and h > 0 , "arbitary arguments must be of type int and value mustbe greater than 0"
     
    totalArea = (l * b * h) / 3

    return round(totalArea,3) 


print(calaculateAreaRec2(b = 3.121322323,l = 3,h = 4))




def calaculateAreaRec3(l = 2,b = 3,h = 6):
    
    assert type(l) == int and l > 0 and b > 0 and h > 0 , "arbitary arguments must be of type int and value mustbe greater than 0"
     
    totalArea = (l * b * h) / 3

    return round(totalArea,3) 


print(calaculateAreaRec3())


def calaculateAreaRec3(l,b,/,*,h):
    
    assert type(l) == int and l > 0 and b > 0 and h > 0 , "arbitary arguments must be of type int and value mustbe greater than 0"
     
    totalArea = (l * b * h) / 3

    return round(totalArea,3) 


print(calaculateAreaRec3(11,34,h = 21))


from numbers import Number
def calcualtesumofNumbers(a,b,c = 10.12):
    assert isinstance(a,Number) and isinstance(b,Number) and isinstance(c,Number)
    sum = 0
    numbers = [a,b,c]
    
    for x in numbers:
        sum += x
    
    print(f"Sum of three numbers is:{sum:.3f}")   
    return sum


print(calcualtesumofNumbers(b=3.2323,a=1.3443))