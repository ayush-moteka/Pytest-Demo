




#We create a new file using "x" mode --> It creates a new file , if file already exists it will throw an error

#Using Excepting handling checking if file exists then create a new one and if doesnt then create a new file 


try:
    f = open("Python Modules/File Handling/dems.txt", "x")
except FileExistsError as fe:
    print(f"{fe} — File already exists. Creating a new one as 'zepters.txt'")
    f = open("Python Modules/File Handling/zepters.txt", "x")
else:
    print("File 'dems.txt' created successfully.")
    
    

   


