


#For opening a file we have open () function that takes in 2 paramenters --> filename and mode of the file

# --> open(filename,mode)

#Different modes are: 
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""


f = open("Python Modules/File Handling/names.txt","rt")

print(f.read()) #Will read and print the entire file
#print(f.close()) #Will close the file

#Other way to open files with the with statement -->The advantage with the with statement is that there is no need to close the files


with open("Python Modules/File Handling/names.txt","rt") as fe:
    print(fe.read()) 


#There is another readline method which is used to read only a single line from the text, it can be called multiple times if needed

with open("Python Modules/File Handling/names.txt","rt") as f:
    print(f.readline()) #Prints the first line
    print(f.readline()) #Prints the next line
    

#Can also fetch the data from file based on the characters

with open("Python Modules/File Handling/names.txt","rt") as f:
  print(f.read(5)) #Will fetch the first 5 characters of the txt


with open("Python Modules/File Handling/names.txt","rt") as x:
   for z in x:
      print(z,"Each line inside the file ")




with open("Python Modules/File Handling/testers.txt","w") as f:
    f.write("Hello my name is Ayush Moteka and I live in vizag..")
    

with open("Python Modules/File Handling/testers.txt","rt") as f:
  print(f.read())

import json

try:
 with open("Python Modules/File Handling/newhops.json","x") as f:
  jsonfile = {
       "customers":[
         {
           "firstname":"Brendon",
           "lastname":"Mccullum"
         },
         {
           "firstname":"Bristpl",
           "lastname":"Latest"
         }
       ],
       "non-customers":[{
         "isPresent":True,
         "offset":"Yes"
       }]
     }
  json.dump(jsonfile,f,indent=2)
  print("New File created with the required json data..")
  
except FileExistsError as fe:
  print(f"{fe} Please check in your ")
  