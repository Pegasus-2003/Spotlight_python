#Counting the number of lines starting with A
f=open("poem.txt",'r')
s=f.readlines()
c=0
for i in s:
    if i[0]=="A" or i[0]=="a":
        c+=1
print(c)
