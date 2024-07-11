file=open("POEM.txt",'r')
x=0
for i in file:
    x+=len(i)
print(x)
file.close()
