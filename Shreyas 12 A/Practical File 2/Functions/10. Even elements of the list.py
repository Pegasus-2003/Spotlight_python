# To get all the even elements of the list
def even(l):
    e=[]
    for i in l:
        if i%2==0:
            e.append(i)
    return e	
L=eval(input("Enter the list "))
h=[]
h=even(L)
for i in h:
    print(i)
