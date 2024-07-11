#Seaching element using binary search
def search(l,k):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==k:
            return mid
        elif l[mid]>k:
            high=mid-1
        else:
            low=mid+1
    return -1
d=[]
n=int(input("Enter the number of terms "))
for i in range(n):
    s=int(input("Enter the item "))
    d.append(s)
k=int(input("Enter the number to be searched "))
j=search(d,k)

if j!= -1 :
    print("At position",(j+1))
else:
    print("Not found ")
