#program to convert a given number of days into months and days and also display the remaing days in a month
n=int(input("Enter the number of days : "))
m=n//30
d=n%30
print(m,"months",d,"days")
print("Remaining days : ",(30-d))
