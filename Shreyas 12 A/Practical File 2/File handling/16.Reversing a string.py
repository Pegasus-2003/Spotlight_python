# Reversing a String
def reverse(l):
    f=open(l,'r')
    s=f.read()
    le=len(s)
    s1=''
    for i in range((le-1#),-1,-1):
        s1+=s[i]
    print(s1)
reverse("input.txt")
