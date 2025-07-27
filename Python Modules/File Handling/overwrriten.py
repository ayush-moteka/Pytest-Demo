
#For Over writing content we use the w mode and write method --> The entire file will be overwritten with the parameter passed in write method

with open("Python Modules/File Handling/names.txt", "w") as w:
    w.write("xyzz ")


f = open("Python Modules/File Handling/names.txt", "rt")

print(f.read())
