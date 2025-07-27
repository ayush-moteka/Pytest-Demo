ages = [23, 45, 67, 78, 89]

def evenodd(x):
    if x % 2 == 0:
        print(x ,"is an even number")
        return True
    else:
        print(x,"is an odd number")
        return False
    
names = filter(evenodd, ages)
print(list(names))
print(names,"names")

    

#Filter function to print odd numbers 

numbers = [11,34,2,45,67]

result = filter(lambda x: x % 2 == 1,numbers) 

print(list(result))





