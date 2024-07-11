#Removing lines starting with "a" from one file and writing it into another file
f=open("Answer.txt",'r')
s=f.readlines()
l=[]
l1=[]
for i in s:
    c=1
    if 'a' in i:
        l.append(i)
    else:
        l1.append(i)
h=open("answer1.txt",'w')  
h.writelines(l1)
h=open("answer1.txt",'r')
print(h.read())
g=open("answer2.txt",'w')  
g.writelines(l)
g=open("answer2.txt",'r')
print(g.read())

