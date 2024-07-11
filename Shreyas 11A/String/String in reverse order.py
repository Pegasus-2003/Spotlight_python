#String in reverse order
string=input("Enter a string")
l= len(string)
for i in range(-1,(-l-1),-1):
    print(string[i])
