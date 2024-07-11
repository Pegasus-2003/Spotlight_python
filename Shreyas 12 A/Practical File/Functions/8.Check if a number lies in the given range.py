# To check if a number lies in the given range
def range(l,u,n):
    p=0
    if n>=l and n<=u:
        p=1
    return p
up=int(input("Enter the upper limit "))
lo=int(input("Enter the lower limit "))
no=int(input("Enter the number to be checked "))
s=range(lo,up,no)
if s==1:
    print("It lies in the range")
else:
    print("It doesnt lie in the range")
