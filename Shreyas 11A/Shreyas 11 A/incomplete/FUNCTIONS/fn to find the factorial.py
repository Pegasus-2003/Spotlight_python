def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return(f)
m=int(input("Enter a number: "))
print(fact(m))
        
