#Program to sum the odd elements in a list
def odd_sum(l):
    s=0
    for i in l:
        if i%2==1:
            s+=i
    return s
L=eval(input("Enter the list "))
S=odd_sum(L)
print(S)
            
