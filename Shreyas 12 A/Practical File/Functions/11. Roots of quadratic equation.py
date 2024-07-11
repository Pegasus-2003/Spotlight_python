# Program to get the roots of a quadratic equation
def quad(a,b,c):
    D=(b**2)-4*a*c
    x1=(-b-D)/2*a
    x2=(-b+D)/2*a
    return x1,x2	
A=int(input("Enter the coefficient of x^2 "))
B=int(input("Enter the coefficient of x "))
C=int(input("Enter the constant term "))
r1,r2=quad(A,B,C)
print("The roots of the quadratic are”,r1,"and",r2)
