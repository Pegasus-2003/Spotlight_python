#Longest word of a given file
def stats(n):
    f=open(n,'r')
    s=f.read()
    l=s.split()
    m=l[0]
    M=len(m)
    for i in range(1,len(l)):
        h=l[i]
        if len(h)>M:
            m=h
            M=len(m)
    print(m,M)
s=input("Enter file name")
stats(s)
