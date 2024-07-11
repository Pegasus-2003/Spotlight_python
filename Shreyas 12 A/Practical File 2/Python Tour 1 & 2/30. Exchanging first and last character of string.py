#Exchanging first and last character of a string
a=input("Enter the string :")
l=len(a)
s=a[l-1]
for i in range(1,l-1):
    s+=a[i]
s1=s+a[0]
print("Entered string :",a)
print("Converted string :",s1)
