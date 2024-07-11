#Sum of the Square of the digits of a number
def digit(n):
    s=0
    while n>0:
        t=n%10
        s+=(t**3)
        n=n/10
N=int(input("Enter the value "))
digit(N)
