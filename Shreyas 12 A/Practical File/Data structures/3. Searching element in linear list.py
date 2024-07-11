#Searching element linear list
def search(l,k):
    le=len(l)
    for i in range(le):
        if l[i]==k:
            return i
    return None
d=[]
n=int(input("Enter the number of terms "))
for i in range(n):
    s=int(input("Enter the item "))
    d.append(s)
k=int(input("Enter the number to be searched "))
j=search(d,k)
if j!=None:
    a=j+1
    print("At position",a)
else:
    print("Not found ")
