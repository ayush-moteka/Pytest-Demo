
#Global Variable
x = "Ayush"

def glob():
    print("My Name is: " + x)

glob()


y = "Good Man"

def glob2():
    y = "Bad Man"
    print(y,"y")

glob2()
print(y,"y2")


def glob3():
    global z
    z = "Wonderful"

glob3()
print('z is'+" "+ z)

