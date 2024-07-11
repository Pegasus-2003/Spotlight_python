#program to accept time in seconds and print in hours and minutes
a=int(input("Enter time in seconds :"))
h=int(a/3600)
m=int((a-(h*3600))/60)
print(h,"Hours : ",m,"Minutes")
