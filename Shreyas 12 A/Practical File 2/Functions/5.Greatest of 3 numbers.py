#Program to find the maximum of 3 numbers
def max(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    elif z>=x and z>=y:
        return z
a=int(input("Enter the 1st number "))
b=int(input("Enter the 2nd number "))    
c=int(input("Enter the 3rd number "))
h=max(a,b,c)
print("The max= “,h)

