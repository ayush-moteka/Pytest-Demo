

#Loop through all the characters of the string 
message = "HelloAyush"

for x in message:
    print(x,"x")
    if x == "s":
      continue
    else:
       print(x.strip())


#Loop through all the items of the list
trips = ["India","Manali","Shimla",None]

for idx,x in enumerate(trips): #Access both index and values of the List or the iterable object.
   print(idx)
   if idx == 0 and x == "India":
      print(f"Yes at index{idx} the value is {x.upper()} ")
   elif x is None:
      print(f"Yes there is an element at index{idx} which of type None and the elemnt is {x}")
   else:
      print("Remaining Values.....")



#Loop through the index of the list

checkLists = ["Satisfactory","Unsatisfactory","New",False]

for x in range(len(checkLists)):
    if x == 2:
       print(f"The element at index {x} is {checkLists[x].upper()}")
    elif x == 3 and isinstance(checkLists[x],bool):
       print(f"This element at index{x} is of type boolean and its value is {checkLists[x]}")
    else:
       print("Remaining.......")


#Using continue and break statement to skip and stop the loop


steps = [{
   "name":"ret"
},"dff",False,None]


for x in steps:
    if isinstance(x,dict) and x.get("name") == "ret":
       continue
    print(x)



cities = [{"name","okay"},(False,"okay","world"),"trips"]

for z in cities:
    if isinstance(z,tuple):
       newlist = list(z)
       newlist[1:3] = ["Water","Sand"]
       newtuple = tuple(newlist)
       print(newtuple,"newupdated tuple")
    elif isinstance(z,set) and len(z) > 1:
       z.add("Buddy")
       print(z,"newupdatedset")
    else:
       break




    #Nested for loop


    a = ["x","y","z"]

    b = ["v","x","s"]


    for x in a:
       print(x,"currentval")
       for y in b:
          print(x + "-" + y)