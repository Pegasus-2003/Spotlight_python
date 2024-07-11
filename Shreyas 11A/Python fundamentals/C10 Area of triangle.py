#Program for area of trinagle
A= int(input("Enter side 1 :"))
B=int(input("Enter side 2 :"))
C=int(input("Enter side 3 :"))
S=(A+B+C)/2
Ar=(S*(S-A)*(S-B)*(S-C))**0.5
print("The area of the triangle is",Ar,"sq.units")
