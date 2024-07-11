# Program to calculate the product of all elementa of the list
def product(l):
    p=1
    for i in l:
        p*=i
    return p
list1=eval(input("Enter the list "))
h=product(list1)
print("The product of all elements in the list is”,h)
