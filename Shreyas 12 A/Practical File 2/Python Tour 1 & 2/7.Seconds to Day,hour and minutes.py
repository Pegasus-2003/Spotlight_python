# Program to convert given seconds to day, hours, minutes and seconds
s=int(input("Enter seconds :"))
d=s//(24*3600)
s=s%(24*3600)
h=s//3600
s=s%3600
m=s//60
s=s%60
print("Days",d,"hours",h,"minutes",m,"seconds",s)

