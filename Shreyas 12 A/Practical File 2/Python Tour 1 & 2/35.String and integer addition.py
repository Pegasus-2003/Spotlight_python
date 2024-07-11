#Program that adds the integer and the digits extracted from a string
a=int(input("Enter the integer :"))
b=input("Enter a string :")
l=len(b)
s=0
for i in range(l):
    if b[i].isdigit():
        s+= float(b[i])
digits=int(s)
print("Integer input + string digits =", a +digits )
