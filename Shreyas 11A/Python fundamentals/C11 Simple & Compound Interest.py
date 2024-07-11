#program to find simple interest and compound interest
p=int(input("Enter principle amount :"))
t=int(input("Enter time (In years) :"))
r=int(input("Enter rate per annum :"))
SI=p*t*r/100
CI = p*((1 + (r/100))**t)
print("Simple Interset =",SI)
print("Compound Interest =",CI)
