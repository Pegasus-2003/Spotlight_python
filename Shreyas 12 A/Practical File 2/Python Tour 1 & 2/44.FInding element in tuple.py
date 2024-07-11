#Searching element in tuple
t=eval(input("Enter a tuple :"))
char=input("Enter the character to search :")
if char in t:
    count=0
    for i in t:
        if i!=char:
            count+=1
        else:
            break
    print(char,"is at index",count)
    
else:
    print(char,"is not in ",t)
