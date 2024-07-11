#program to accept the days and express in years, months and days
a=int(input("Enter no of days :"))
y=int(a/360)
b=a-(y*30*12)
m=int(b/30)
d=int(b-(m*30))
print(y,"Years : ",m,"Months : ",d,"Days")
