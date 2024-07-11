#Copying file and replacing 2 consecutive blank spaces with one
def copy(n,l):
    f=open(n,'r')
    s=f.read()
    le=len(s)
    s1=""
    i=0
    while i<le:
        if s[i]=="" and s[i+1]=="":
            s1+=""
            i+=2
        else:
            s1+=s[i]
            i+=1
    f.close()
    f=open(l,'w')
    f.write(s1)
copy(“Report.txt","copy1.txt")
