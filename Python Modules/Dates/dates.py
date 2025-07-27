

#In Python we dont have a built in data type for Dates but we have a module names datetime to work with Dates as objects


import datetime

x = datetime.datetime.now()


print(x.year) #2025
print(x.strftime("%A")) #Wednesday


y = datetime.datetime(2025,6,4)


print(y.year)
print(y.month)
print(y.day)
print(y.date())


print(y.strftime("%A")) #WeekDay
print(y.strftime("%w")) #Week day as number -- 0 is Sunday 
print(y.strftime("%d")) #Day of the month
print(y.strftime("%B")) #Month Name 
print(y.strftime("%Y"))

