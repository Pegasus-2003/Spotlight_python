# Insertion sort
l=eval(input("Enter a list :"))
print("Original list is :",l)
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=key
print("List after sorting :",l)
