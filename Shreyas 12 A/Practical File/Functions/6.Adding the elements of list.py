# Program to add all the elements of the list
def sum(l):
    s=0
    for i in l:
        s+=i
    return s
list1=eval(input("Enter the list "))
h=sum(list1)
print("The sum of all elements in the list is”,h)


