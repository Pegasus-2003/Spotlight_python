n=int(input("Enter number of names: "))
d={}
for i in range (0,n):
    s=input("Enter name: ")
    p=int(input("Enter percentage: "))
    d[s]=p
print(d)
s1=input("Enter the name to be deleted: ")
del d[s1]
print (d)

