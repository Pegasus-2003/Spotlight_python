def sum(n):
    s=0 
    for i in range(1,2*n+1,2):
        s+=i
    return(s)
a=int(input("Enter a number: "))
print(sum(a))
        
