



#JSON --> Javacript Object Notation is a data exchange format between the client and server

#It is a syntax for storing and exchanging data



#Parse or convert JSON to Python using loads method and the result will be a Python dictionary

import json

x = '{"name":"Ayush","city":"Vizag","country":"India","age":23}'

y = json.loads(x)

y["name"] = "Tarun"

y.update({"book":"New Legacy Begins"})
print(y,"resultpythondict") #Result is a Python Dictionary with single quotes
print(type(y),"type") #Result is a dict  <class 'dict >


#Convert from Python to JSON using dumps() method  --> the result is json object


cricketers = {"name":"ViratKohli","subcricketers":{"world":"yes","it":False},"city":"Vizag","isIPL":True}

jsondata = json.dumps(cricketers)

print(jsondata,"jsondata") #Result is a JSON object with double quotes 

print(type(jsondata),"type") #Result is string type <class 'str'>



#In Short we are just converting python data types to Javascript data types



print(json.dumps("Ayush")) #str to String
print(json.dumps(23)) #Int to Number
print(json.dumps(23.23)) #Int to Number
print(json.dumps(False)) #bool to false
print(json.dumps(True)) #bool to true
print(json.dumps("")) #str to String
print(json.dumps({"name0":"Brendon","city":"Vizag"})) #Dict to object
print(json.dumps([{"name":"Ayush"},12,23,"World"])) #List to Array
print(json.dumps(("Ayushers",))) #Tuple to Array
print(json.dumps(None)) #None to null



#Example to convert a dict which consits of all data types to JSON using dumps method 



test = {
    "name":["Hello","Wish"],
    "age":21,
    "city":"Vizag",
    "company":False,
    "isWorth":True,
    "tuple":("trip","nontrip"),
    "float":"12.32",
    "none":None,
    "buddy":"Kartik"
}
print(json.dumps(test,indent = 4 ,sort_keys = True))
print(type(json.dumps(test))) #<class 'str'>




#Ex:4 


import json
test = (dir(json))
print(test,"tes")
try:
    list1 = {"name":"Ayush","city":"Vizag","age":30}
    json_str = json.dumps(list1) #Convert from PYTHON TO JSON
    json_dict = json.loads(json_str) #Convert from json to python
    if not (isinstance(json_dict,dict) and len(json_dict) > 0):
        raise TypeError(f"{json_dict} is not a result python dictionary")
    if not (isinstance(json_str,str) and len(json_str) > 0):
        raise TypeError(f"{json_str} is not a result python dictionary")    

except (TypeError,json.JSONDecodeError)as ter:
      print(f"{json_dict} is not a valid dictionary {ter}")
      print(f"{json_str} is not a valid dictionary {ter}")
else:
    print(json_dict,"jsonresultdict")
    print(json_str,"jsonocject")





