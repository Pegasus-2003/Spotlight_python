# Second largest element of a tuple
t=eval(input("Enter a tuple of numbers :"))
large=max(t)
length=len(t)
slarge=0
for i in range(length):
    if slarge < t[i]<large:
        slarge=t[i]
print("Second largest element :",slarge)
