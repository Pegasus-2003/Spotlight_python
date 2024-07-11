# Counting the no of characters upto the first 'S'
def count(n):
    c=0
    f=open(n,'r')
    s=f.read()
    n=len(s)
    for i in range(n):
        if s[i]=="$":
            print(i+1)
            break
        elif i==(n-1):
            print("NOT FOUND")


n=input("Enter the name to be checked ")
count(n)
