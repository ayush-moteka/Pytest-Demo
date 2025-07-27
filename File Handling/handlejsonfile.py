import json

filepath = "C:/Users/info/Desktop/Python Practice/Python Modules/File Handling/customers.json"

with open(filepath, "rt") as f:
    pythondict = json.load(f)  # use json.load for file objects
    print(type(pythondict))    # should print: <class 'dict'>
    print(pythondict)
    
    pythondict.update({"username":"Ayush-Admin"})
   
    for x in pythondict:
        print(x,"xx")


try:

 f = open("C:/Users/info/Desktop/Python Practice/Python Modules/File Handling/test.txt","x")

except FileExistsError as fe:
    print(f"{fe} Please create a new file with different name.")
    
    with open("C:/Users/info/Desktop/Python Practice/Python Modules/File Handling/testnew.txt","x") as f:
     with open("C:/Users/info/Desktop/Python Practice/Python Modules/File Handling/testnew.txt","a") as f:
        f.write("Hello new file is created with name testnewtext")

else:
    with open("C:/Users/info/Desktop/Python Practice/Python Modules/File Handling/test.txt","a") as f:
        f.write("Hello new file is created with name test")
            



       
    
