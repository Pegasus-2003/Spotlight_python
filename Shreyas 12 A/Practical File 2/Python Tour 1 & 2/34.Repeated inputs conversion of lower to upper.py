#Program that repeatedly inputs string and converts lowercase to uppercase and vice-versa
s=""
while True:
    ch=str(input("Enter the character (q to quit):"))
    if ch=="Q" or ch=="q":
        break
    else:
        l=len(ch)
        for i in range(l):
            if ch[i].isupper():
                s+=ch[i].lower()
            elif ch[i].islower():
                s+=ch[i].upper()
            else:
                s+=ch[i]
        print("Converted string :",s)
