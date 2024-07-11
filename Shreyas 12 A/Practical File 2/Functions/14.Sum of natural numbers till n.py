#Program to find to sum of natural numbers till n
def SUM(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
a=int(input("Enter the number to be calculated "))
print("The sum of all natural numbers until”,a,"is",SUM(a))

