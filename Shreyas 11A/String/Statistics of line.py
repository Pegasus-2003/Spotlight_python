#Statistics of a line
string=input("Enter a string")
l= len(string)
lowercount=digitcount=0
uppercount=alphacount=0
for i in string:
    if i.islower():
        lowercount+=1
    elif i.isupper():
         uppercount+=1
    elif i.isdigit():
        digitcount+=1
    if i.isalpha():
        alphacount+=1
print("Number of alphabets :",alphacount)
print("Number of digits :",digitcount)
print("Number of uppercaseletters:",uppercount)
print("Number of lowercase letters :",lowercount)

    
    
