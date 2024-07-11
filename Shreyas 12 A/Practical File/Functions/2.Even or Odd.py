#Program to check if the given number is even or odd
def odd(x):
    if x%2==0:
        i=0
    else:
        i=1
    return i
n=int(input("Enter the number to be checked "))
h=odd(n)
if n==0:
    print("IT IS EVEN ")
else:
    print("IT IS ODD”)

