#removing vowels for the entered string
a=input("Enter a string")
vowels=['a','i','e','o','u']
for i in a :
    if i not in vowels:
        print(i,end="")
