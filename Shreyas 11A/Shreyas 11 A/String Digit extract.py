#string extract of digits
string=input("Enter a string")
c=0
s=0
for a in string:
    if a.isdigit():
        print(a)
        s=s+int(a)
        c=c+1
if c==0:
    print("String has no digit")
else:
    print("Sum of digits is :",s)
