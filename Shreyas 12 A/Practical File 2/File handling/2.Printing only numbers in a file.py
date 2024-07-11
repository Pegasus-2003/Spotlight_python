#Printing only numbers
f=open("poem.txt",'r')
s=""
c=0
while s:
    s=f.readline()
    for i in s:
        if i.isnumeric():
            c+=1
print(c)
f.close()
