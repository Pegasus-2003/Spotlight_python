#Largest element of a list
l=eval(input("Enter a list :"))
length=len(l)
max=l[0]
index=0
for i in range(1,length):
    if l[i]>max:
        max=l[i]
        index=i
print("The largest element of the list : ",max," found at index",index)
