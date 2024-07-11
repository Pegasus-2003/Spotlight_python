def d(m):
    s=1
    for i in range(2,m+2,2):
        s=s+1/i
    return(s)
n=int(input("Enter a number: "))
print(d(n))
      
