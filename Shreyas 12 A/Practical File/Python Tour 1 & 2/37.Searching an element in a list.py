#Searching an element in a list
l=eval(input("Enter a list :"))
length=len(l)
a=int(input("Enter the element to be searched :"))
for i in range(1,length):
    if l[i]==a:
        print("The element found ",a," was found at index ",i)
        break
else:
    print("The element was not found")
