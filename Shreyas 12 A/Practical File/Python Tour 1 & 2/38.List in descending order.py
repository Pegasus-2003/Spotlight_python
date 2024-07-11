#List in descending order
l=eval(input("Enter a list :"))
length=len(l)
for i in range(1,length):
    ele=l[i]
    j=i-1
    while j >=0 and ele< l[j]:
        l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=ele
for i in range(int(length/2)):
    a=l[i]
    l[i]=l[length-i-1]
    l[length-i-1]=a
print("List in descending order :",l)
