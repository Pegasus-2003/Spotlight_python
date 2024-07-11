#Program to find arithmetic mean
def am(l):
    s=0
    for i in l:
        s+=i
    a=s/len(l)
    return a
lis=eval(input("Enter the list "))
print("The arithmetic mean of the list is “,am(lis))

