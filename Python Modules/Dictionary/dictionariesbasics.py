

#It is a build in data type which stores the values in the form of key and value pairs. 
#Create a new dictionary using general way
checklists = {
    "name":"Restful",
     "id":2023,
     "price":12.34,
     "isPresent":False,
     "isAvaialble":True,
     "isDone":None,
     "subchecklist":[{
         "world":"India",
         "city":"Vizag"
     }]
}

#Check if key exists in a dictionary
for x in checklists:
  if "name" in x:
    print("Yes name key exists in checklists dictionary")
  elif len(x) > 2 and isinstance(x,str):
     print(f"Yes this key length is greater than 2 and it is {x}")
  else:
     print("zzzz")

#Create a new dictionary using dict constructor
newDict = dict(name = "Ayush",city = "Ahmedabad",country = "Spain")

#Fetch the dictionary values using get method
values = checklists.get("name")

#Fetch the keys using keys method
keys = checklists.keys()

#Fetch the values of dict using values method
values = checklists.values()
checklists["isPresent"] = True
checklists["id"] = 2012
for x in values:
    if x == "Restful":
        print(f"Yes this dict has a value names {x}")
    elif isinstance(x,bool):
        print(f" Yes this value if of type Boolean {x}")
    else:
        print(f"The remanining names of the keys are:{x}")


#Fetch the items of dict means both keys and values using items method

items = checklists.items()

for y,z in items:
    print(f"The keys are {y} and values of dict are {z}")


#Using update method update the dictionary by passing arguments as a dict or an iterable object

checklists.update({"color":"ornage","number":1})
print(checklists,"cc")


#Remove items from a dictionary

checklists.pop("color")
print(checklists,"deleted")

#Remove last item from dictionary
checklists.popitem()
print(checklists,"lastelement")

#Remove using delete keyword we can remove using the key as well as can delete the entire dictionary also

"""
del checklists["price"]
del checklists
"""


#Clear the entire dictionary by using clear method 
checklists.clear()
print(len(checklists))


#Set default value of the key to a particular one, if value is not given then by default None is returned in value
a = checklists.setdefault("name","Ayush Moteka")
b = checklists.setdefault("x","yes")

print(checklists,"y")

#Create a new dictionary by defining the keys customly 


z = checklists.fromkeys(("one","three","seven"),3)
print(z,"z")

key = ("cricket","hockey","volleyball")
value = "sports"

resultdict = dict.fromkeys(key,value)
print(resultdict,"resultdic")
assert len(resultdict) == 3

for x in resultdict.keys():
    if x == "hockey" and isinstance(x,str):
       print(f"{x} is the National Sport of India")
    else:
       print(f"Other sports that are played in india are :{x}")

#Using Loops Iterate over all the elements over dictionary

names = {
   "pname":"Ayush",
   "lname":"Moteka",
   "id":247,
   "college":"Gitam University",
   "city":"Vizag"
}

for x in names:
   print(x.upper(),"names")

#Iterate through all the keys of the dict -

keys = names.keys()

for x in keys:
   print(x.lower())

#Iterate through all the values 

values = names.values()

for y in values:
   if isinstance(y,str):
     print(f"The values of the dict are {y.lower()}")
   else:
      print(f"This is a value of dict which is not type of string :{y}")


#Iterate through all the keys and values of the dict

for a,b in names.items():
    print(f"The keys of dict {a} and values are {b}")



#Create a copy of an existing dictionary

newCopydict = names.copy()
print(newCopydict,"newcopy")

newCop = dict(names)
print(newCop,"newcop")


#Nested dictionaries

nesteddictionary = {
   "child1":{
      "one":"first",
      "two":"second"
   },
    "child2":{
      "three":"first",
      "four":"second"
   },
    "child3":{
      "five":"first",
      "six":"second"
   }
}

nesteddictionary["child2"]["three"] = "hundred"
print(nesteddictionary,"updateddict")

for n, m in nesteddictionary.items():
    print(n, "keys")
    print(m, "values")
    for r in m:
        print(r,"rr")
        print(r + ":" + m[r])








