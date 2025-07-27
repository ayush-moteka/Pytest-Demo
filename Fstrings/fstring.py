

#Fstrings --> Formattable strings were introduced  --> {} is a placeholder --> It can include variables,functions,modifiers etc
price = 100

tax = 21

text = f"Ayush purchased a bottle of price {price} and the tax is {price + (price * tax)/ 2}"

print(text) if len(text) > 0 else print("String must be greater than zero") if len(text) < 0 else print("Text is not a valid string data type")


#Modifiers are added after a semi colon : 

chocolate = f"The chocolate is of discount {23:.3f} and its original price is 123"

print(chocolate)


#Add if else statement in placeholders 
discount = 5
bags = f"THe bag i ordered is: {"Expensive" if discount > 1 else "Cheap"}"
print(bags)

#Use a function to print the value from a function in a formattable string

def printfinalrice(x,y):
    finalprice = x * (x + y)/2
    return finalprice

z = f"The final price is {printfinalrice(21,34):.2f}"

print(z,"z")

#Use comma as a thousand seperator or an underscore as a thousand seperator
value = 18223
formattedresult = f"{value:,}" if value <= 15000 else f"{value:_}"
icecreams = f"The icecream is my favourite one and its value is :{formattedresult}"
print(icecreams,"icecreams")


#Before Version Python 3.6 we used to Format strings using format() method

quantity = 23
discountedRate = 11
finalRate = "The wall has a ceiling of price {} and its discount is {:.2f} dollars"

print(finalRate.format(quantity,discountedRate))