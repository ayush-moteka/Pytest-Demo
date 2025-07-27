

#To delete a file we need to import an os module there is no mode and no need to use open method.
from os import path
from os import remove

if path.exists("Python Modules/File Handling/zepters.txt"):
       remove("Python Modules/File Handling/zepters.txt")

else:
     print("File does not exists , Please check the file in your directory")


#to delete an entire folder we can use rmdir() method


from os import rmdir

print(rmdir("Here specify the path of the folder that contains the file to be deleted"))

    

