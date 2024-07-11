def b(m):
    s=0
    for i in range(12,12*m+1,10):
        s+=i
    return(s)
n=int(input("Enter a number: "))
print(b(n))
    
