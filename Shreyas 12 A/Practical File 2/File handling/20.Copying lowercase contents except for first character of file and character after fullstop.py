#Copying lowercase contents except for first character and character after full stop
def copy(l,n):
    f=open(l,'r')
    s=f.read()
    s=s.lower()
    le=len(s)
    s1=""
    i=0
    while i<le:
        if i==0:
            s1+=s[i].upper()
            i+=1
        elif s[i]==".":
            s1+=". "+s[i+2].upper()
            i+=3
        else:
            s1+=s[i]
            i+=1
    f.close()
    f=open(n,'w')
    f.write(s1)
copy("Report.Txt","finerep.txt")
