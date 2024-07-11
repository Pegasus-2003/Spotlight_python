#Finding the Most commomly occuring word
f=open("india.tv",'r')
s=f.read()
d={}
w=s.split()
for i in w:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(i,d[i])

