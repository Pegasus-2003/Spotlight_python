#Add  "ing" if length is 3, add "ly " is string already ends with ing ,if length is less than 3 let it be unchanged
a=input("Enter the string :")
l=len(a)
s=""
s1=""
s= a[l-3] +a[l-2]+a[l-1]
if l==3:
    s1=a+"ing"
elif  s=="ing" or s=="ING":
        s1=a + "ly"
else:
    s1=a
print("Entered string :",a)
print("Converted stirng :",s1)
