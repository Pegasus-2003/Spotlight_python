#Printing content of TELE in 2 column
f=open("tele.txt",'r')
s=f.read()
l=s.split()
le=len(l)
i=0
while i<le:
    print(l[i],end='\t')
    print(l[i+1])
    i+=2
