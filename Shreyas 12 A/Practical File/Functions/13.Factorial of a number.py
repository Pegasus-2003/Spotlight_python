# Progeam to calculate the factorial of a number
def am(l):
    s=0
    for i in l:
        s+=i
    a=s/len(l)
    return a
lis=eval(input("Enter the list "))
print("The arithmetic mean of the list is “,am(lis))

#prog13
def fact(n):
    p=1
    for i in range (1,n+1):
        p*=i
    return p
a=int(input("Enter the number to be calculated "))
print("The factorial of the number is",fact(a))
