# Bubble sort
l=eval(input("Enter a list :"))
print("Original list is :",l)
for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(" list after sorting :",l)
