def calc(x,y):
    sum1=x+y
    diff=x-y
    prod=x*y
    return(sum1,diff,prod)
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
p,q,r=calc(a,b)
print(p,q,r)
print(calc(a,b))
