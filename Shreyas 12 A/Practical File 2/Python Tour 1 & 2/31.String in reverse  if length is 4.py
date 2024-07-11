#String in reverse order if length is 4
string=input("Enter a string")
l= len(string)
s=""
if l==4:
    for i in range(-1,(-l-1),-1):
        s+=string[i]
    print("Reversed  string :",s)
else:
    print("String  is unchanged")
