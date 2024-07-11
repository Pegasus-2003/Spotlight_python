#Program to calculate the volume of a box
def vol(l,b,h):
    v=l*b*h
    return v
L=int(input("Enter the Length "))
B=int(input("Enter the Breadth "))
H=int(input("Enter the Height "))
V=vol(L,B,H)
print("Volume of the box is”,V)
