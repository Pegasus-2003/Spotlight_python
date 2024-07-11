# inserting in sorted list
import bisect
l=[70,60,50,40,30]
l.reverse()
print(l)
k=int(input("enter new "))
print(bisect.bisect(l,k))
bisect.insort(l,k)
print(l)
