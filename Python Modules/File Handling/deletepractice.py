


import os

try:
     os.remove("C:/Users/info/Desktop/Python Practice/Python Modules/File Handling/testnew.txt")
     print("File Deleted Successfully..")
        
except FileNotFoundError as fe:
     print(f"{fe} Please check the path of the file given the file it does not exists ")
     print("File not found..")

