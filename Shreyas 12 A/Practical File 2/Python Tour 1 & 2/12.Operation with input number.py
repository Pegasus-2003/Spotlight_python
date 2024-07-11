#PROGRAM TO PERFORM THE INPUT OPERATION WITH THE INPUT NUMBERS
n1=int(input("Enter 1st number "))
n2=int(input("Enter 2nd number "))
c=input("Enter the operator ")
a=0
if c=='+':

    a=n1+n2
if c=='i':
    a=n1-n2
if c=='*':
    a=n1*n2
if c=='/':
    a=n1/n2
if c=="//":
    a=(n1//n2)
if c=='%':
    a=n1%n2
print(n1,c,n2,"=",a)

