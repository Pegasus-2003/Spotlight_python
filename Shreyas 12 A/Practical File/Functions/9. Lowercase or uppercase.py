#To check if the given string is lowercase or uppercase
def strin(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    return u,l
S=input("Enter the string")
U,L=strin(S)
print("No of uppercase",U)
print("No of lowercase",L)
