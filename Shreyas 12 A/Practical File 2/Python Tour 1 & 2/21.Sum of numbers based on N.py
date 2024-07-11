#Sum of numbers based on n:
n=int(input("Enter the value :"))
sum=0
if n<0:
    x=-(n)
    for i in range(x,x*2):
        sum+=i
else:
    for i in range(2*n,n,-1):
        sum+=i
print("The sum of numbers :",sum)
