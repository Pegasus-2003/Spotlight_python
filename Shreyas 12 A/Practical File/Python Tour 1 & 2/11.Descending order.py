#PROGRAM TO GET THE DESCENENDING ORDER OF 3 INPUT NUMBERS
x=int(input("Enter the 1st number "))
y=int(input("Enter the 2nd number "))
z=int(input("Enter the 3rd number "))
print("THE DESCENDING ORDER IS")
if x>=y and x>=z:
    if y>z:
        print(x,y,z)
    else:
        print(x,z,y)
elif y>=x and y>=z:
    if x>z:
        print(y,x,z)
    else:
        print(y,z,x)
elif z>=x and z>=y:
    if x>y:
        print(z,x,y)
    else:
        print(z,y,x)
