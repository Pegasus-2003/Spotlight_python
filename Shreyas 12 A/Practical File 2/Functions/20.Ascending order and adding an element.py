# Program to accept a list in ascending order and adding an element
def add(l,n):
    l.append(n)
    return l
def remove(l,n):
    l.pop(n)
    return l
s=[]
L=eval(input("Enter the list in ascending order "))
N=int(input("Enter the number "))
c=int(input("Enter 1 to add or 2 to remove "))
if c==1:
    s=add(L,N)
elif c==2:
    s=remove(L,N)
print(s)
