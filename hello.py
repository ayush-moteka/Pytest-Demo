


def evenodd(*x):
    for num in x:
     if num % 2 == 0:
        print(num,"is an even number")
     elif num % 2 == 1:
        print(num,"is an odd number")
     else:
        print(num,"is neither even nor odd")

evenodd(45,32,23,12,11)