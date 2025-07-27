

names = ("Sachin","Dhoni","Virat")

if "SachinS" in names:
    print("Sachins is not present in names TUPLE")
elif "Dhoni" not in names and "Virat" in names:
    print("Dhoni is not in Names List")
else:
    print("Sachin is present in names")
    
    

list1 = ["Ayushers","tenders",False]

assert False in list1

for x in list1:
    if isinstance(x,bool) and not x == True:
        print(f"Current price is not accurate it is {x}")
    elif "tender" in x:
        print(f"Tender{x} is present in list1")
    elif isinstance(x,str) or len(x) > 0:
        print(f"My name is {x.strip().title()}")
    else:
        print("None of the above")