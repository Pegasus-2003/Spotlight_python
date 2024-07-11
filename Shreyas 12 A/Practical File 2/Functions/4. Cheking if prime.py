# Program to check if a number is prime 
def prime(x):
    n=0
    for i in range(1,x+1):
        if x%i==0:
            n+=1
        if n==2:
            k=1
        else:
            k=0
        return k
N=int(input("ENTER THE NUMBER TO BE CHECKED "))
h=prime(N)
if h==0:
    print("THE NUMBER ISNT PRIME ")
else:
    print("THE NUMBER IS PRIME ")
