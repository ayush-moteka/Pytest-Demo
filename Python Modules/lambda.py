



#Lambda functions are short hand functions --> there can be any numbers of arguments passed but there will be only one expression

#Syntax --> lambda arguments : expression

average = lambda a,b,c: (a + b + c) / 3

print(average(1,2,3))

# Use of anonymous function inside another function
def multiply(x):
    return lambda y : y * x

result = multiply(3)

print(result(2))


product = lambda x,y,z: (x * y * z) / 3
print(product(2,3,4))




