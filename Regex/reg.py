

#Regular Expressions --> THey help us to understand whether a string matches a pattern or not 

import re

txt = "Ayush is from 23 Spain"

ismatched = re.search("^Ayush.*Spain$",txt) #Will return an Match object that contains the result if not matched then None will be returned
hasAyush = re.search("Ayush",txt)
print(hasAyush.span(),"ayushintext") #0,5

if ismatched: print(f"Yes {txt} contains Ayush and Spain")
else : print("No")

print(ismatched)
print(ismatched.start()) #
print(ismatched.span())  #(0,14)
print(ismatched.string)  #Ayush is from Spain 23
print(ismatched.group()) #Ayush is from Spain



allMatched = re.findall("Ay.*h",txt) #Will return a list of strings that match the pattern
isDigit = re.findall("\d",txt) #Special escape characters to check if a string matches the pattern or not this is for digits (\d)
isSpacing = re.findall("\s",txt) #Special escape characters to check if a string matches the pattern or not this is for spacing (\s)
isparticularRange = re.findall("[0-9]",txt) 
print(allMatched)
print(isDigit)
print(isSpacing)
print(isparticularRange)


#Split method is used to split the values where it matches the pattern
isMatch = re.split('\s',txt)
print(isMatch)


#Sub method is used to replace all the occurences with the match of our choice

isOccurence = re.sub("\d","AMH",txt)
print(isOccurence)


#Match Object 

#Example --> <_sre.SRE_Match object; span=(5, 7), match='ai'>

# - span(5,7) -- > The start index and end index of the matched pattern  
# - 



