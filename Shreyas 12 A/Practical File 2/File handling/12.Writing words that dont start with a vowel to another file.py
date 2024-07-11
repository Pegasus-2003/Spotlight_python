#writing words that dont start with a vowel to another file
def VOWELSWORD(n1,n2):
    f=open(n1,'r')
    s=f.read()
    l=[]
    s1=""
    for i in s:
        if i=="" or i==s[-1]:
            l.append(s1+' ')
            s1=""
            continue
        else:
            s1+=i
    f.close()
    f=open(n2,'w')
    s=['A','E','I','O','U']
    for i in l:
        if i[0] in s:
            continue
        else:
            f.write(i+'\n')
    f.close()
    f=open(n2,'r')
    print(f.read())
    print(l)
m1=input("Enter the file to be referred to")
m2=input("Enter the file to be printed to")
VOWELSWORD(m1,m2)
