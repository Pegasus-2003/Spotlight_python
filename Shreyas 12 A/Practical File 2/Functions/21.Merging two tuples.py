#Program to form a list by acepting two tuples
def tup(t1,t2):
    s=[]
    for i in t1:
        s.append(i)
    for i in t2:
        s.append(i)
    h=tuple(s)
    return h
n=eval(input("Enter the first tuple "))
m=eval(input("Enter the second tuple "))
h=tup(n,m)
print(h)
