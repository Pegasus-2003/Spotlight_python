def abc(x,y,z):
	t=x+y-z
	return(t)
a=int(input("Enter a no.: "))
b=int(input("Enter second value: "))
c=int(input("Enter third value: "))
print(abc(a,b,c))
print(abc(x=2,y=4,z=5))
print(abc(y=4,x=2,z=3))
print(abc(10,20,c))
print(abc(10,20*b,c))
