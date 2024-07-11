#TO FIND THE HCF AND LCM OF 2 NUMBERS
a=int(input("Enter the 1st number "))
b=int(input("Enter the 2nd number "))
if a>b:
    small=b
elif b>a:
    small=a
for i in range(1,small+1):
    if (a%i==0) and (b%i==0):
        hcf=i
lcm=(a*b)/hcf
print("LCM IS",lcm)
print("HCF IS",hcf)
