# TELEPHONE DAT
f=open("tele.dat",'r')
print("NAME","%15s" % "NUMBER")
s=f.readlines()
for i in s:
    k=i.split()
    print(k[0],"%15s" % k[1])
