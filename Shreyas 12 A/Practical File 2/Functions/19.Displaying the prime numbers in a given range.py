#Program to print the prime numbers in the given range
def prime(n):
    for i in range(2,n+1):
        s=0
        for j in range(1,i+1):
            if i%j==0:
                s+=1
        if s==2:
            print(i)
n=int(input("Enter the number "))
prime(n)
