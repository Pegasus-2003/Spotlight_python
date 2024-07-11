#Fibonacci series
def fibo(n):
    a=1
    b=1
    print(a,",",b,end=", ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=", ")
        a,b=b,c
a=int(input("Enter the number of terms in the series "))
fibo(a)
