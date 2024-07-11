#Longest and shortest word in NOTES.TXT
f=open("NOTES.txt",'r')
s=f.read()
l=s.split()

def max(l):
    M = l[0]
    m = len(M)
    for i in l:
        if len(i)>m:
            M=i
            m=len(i)
    print(M)
def min(l):
    M = l[0]
    m = len(M)
    for i in l:
        if len(i) < m:
            M = i
            m = len(i)
    print(M)
max(l)
min(l)
