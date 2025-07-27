#This will append or add the content at the end of the file by using a mode and write method

with open("Python Modules/File Handling/names.txt", "a") as t:
    t.write("Add this at the end of the file")

with open("Python Modules/File Handling/names.txt", "rt") as t:
    print(t.read())