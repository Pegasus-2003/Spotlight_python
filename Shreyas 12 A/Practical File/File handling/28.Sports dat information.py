# SPorts.dat information
f=open("sports.dat",'r')
s=f.readlines()
m=[]
for i in s:
    j=i.split()
    if j[0].lower()=="athletics":
        print(i)
        m.append(i)
f.close()
f=open("athletic.dat",'w+')
f.writelines(m)
f.read()
