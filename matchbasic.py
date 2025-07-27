


name = "Richmond"

age = 23

match name:
    case "World":
        print("Yes name is world")
    case  "Seaford" if age == 34:
        print("Yes name is seaford and age is 34")
    case "Ayush" | "Moteka" | "Internet" if age == 23 and isinstance(age,int):
        print("Yes name is one the above ones and age is of type int and it is 23")
    case "Richmond" if age == 23:
        print(f"Yes name is {name} and age is {age}")
    case _: #This is else means by default statement if none of the above conditions are satisfied.
        print("None of the above conditions are satisfied")

        