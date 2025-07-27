


x = "Ayush"

def lengthString(y):
    if len(y) == 5:
        print("Yes length is 5",y)
    elif len(y) == 3:
        print("No not 5")
    else:
        print("Less than 5")


lengthString(x)


#F-Strings

x = 34

txt = f"My name is Ayush and my age is {x}"

print(txt,"txt")

price = 45

newprice = f"The new price is {price:.3f}"

print(newprice,"newpriceee")

#Escape Characters -- Insert Illegal Characters

text = "Hello My name is Tarun Moteka"

result = f"Okay fine Please \"Explain\" it {text}"

print(result,"resultescape")

text2 = "My world is\\done"
print(text2,"t22")
text3 = "Ayush \t world"
print(text3,"t3")

