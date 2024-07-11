#First common element of two lists
def comm(l1,l2):
    t=False
    if t==False:
        for i in l1:
            for j in l2:
                if i==j:
                    t=True
                    break
    return t
l1=eval(input("Enter the list "))
l2=eval(input("Enter the list "))
s=comm(l1,l2)
print(s)

