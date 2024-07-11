#PROGRAM TO FIND THE SOLUTIONS OF A QUADRATIC EQUATION
a=int(input("Enter the coefficient of x^2 : "))
b=int(input("Enter the coeffeicient of x  :"))
c=int(input("Enter the constant  :"))
x1=(-b+((b**2-4*a*c)**0.5))/(2*a)
x2=(-b-((b**2-4*a*c)**0.5))/(2*a)
print("The roots are",x1,"  ,  ",x2)

