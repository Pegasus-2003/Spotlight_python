#Capitalizing a string if 2 are uppercase in the first 4 characters
a=input("Enter the string :")
l=len(a)
count=0
for i in range(4):
    if a[i]>="A" and a[i]<="Z":
        count+=1
if count>=2:
    a=a.upper()
    print("Capitalized string :",a)
else:
    print("String is unchanged")
