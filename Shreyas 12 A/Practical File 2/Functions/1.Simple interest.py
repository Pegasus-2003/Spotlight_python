#Program for calculating Simple interest
def simpleinterest(p,r,t):
    i=(p*r*t)/100
    return i
P=int(input("Enter the principal "))
R=int(input("Enter the rate "))
T=int(input("Enter the Time "))
I=simpleinterest(P,R,T)
print("Simple Interest =“,I)
