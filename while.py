


tuple1 = ("Ayush",True,False,12.4,"World")


#Using While loop for tuple 
i = 0

while(i < len(tuple1)):
    print(tuple1[i])
    i = i + 1

#Using for loop for tuples.
for x in range(len(tuple1)):
    if x == 0:
        print("Click on unsatisfactory button and this is the required one")
    if isinstance(x,bool):
        print(f"This particular element or item in the tuple is of type boolean and it is {x}")
    if isinstance(x,float) and x < 300.94:
        print(f"THis one is of type float and element is {x} and its index is {tuple1[x]}")
    else:
        print("These are regular elements")



z = 1
while(z < 11):
    print(z,"currentvalue")
    z += 1
    if z == 9:
        continue
    elif z == 3 and isinstance(z,int):
        break
    print(z,"z")
    



