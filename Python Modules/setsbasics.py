



set1 = {"Ayush","Tarun","Kumud"}

set2 = {"World",True,12}

set1.add("Kumuders")

list23 = ["Ginner","Fatima","ErosInternational"]

set1.update(list23) 

#Other methods to remove an element from set are pop , to clear the set we use clear method, to del the set we use del keyword
print(len(set1))




#Join Sets

set4 = {"Virat","Rohit",True,False,0,1}

set5 = {"Hockey","Cricket","Virat","Singh",True,0}

set6 = set4.union(set5,set1,set2) # or you can use | also will give same result but not a new set it will change the existing set

set4.update(set6)

set7 = set4.intersection(set5) #duplicate values or you can use & also

set4.intersection_update(set7)

setnew = set4.difference(set1) #ALL elements of set 4 which are not there in set2 or u can use - operator also
set4.difference_update(set1)#it wont return a new set and the existing set will be changed


setn = set4.symmetric_difference(set1) #non- duplicate elements that are not present in both the sets , you can use ^ opereator also.
set4.symmetric_difference_update(set1)

z = set4.isdisjoint(set1) #Returns true if none of elements are present in both the sets and return False if there are duplicates
a = set4.issubset(set1) #Returns True if all elements of set1 are present in set2 else return false
x = set2.issuperset(set1) #Returns true if all elements of set1 are present in set2 else return false
print(set6)