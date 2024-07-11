#ALL records of line with line number
f=open("poem.txt",'r')
s=" "
c=0
while True:
    s=f.readline()
    if s=="":
        break
    c+=1
    print(c,s,end=" ")
f.close()
