#PROGRAM TO CHECK IF A CHARACTER IS A DIGIT, LOWERCASE , UPPERCASE OR SPECIAL CHARACTER
c=input("Enter the character ")
if c>='a' and c<='z':
    print("LOWERCASE")
elif c>='A' and c<='Z':
    print("UPPERCASE")
elif c>='0' and c<='9':
    print("DIGIT")
else:
    print("SPECIAL CHARACTERS ")

