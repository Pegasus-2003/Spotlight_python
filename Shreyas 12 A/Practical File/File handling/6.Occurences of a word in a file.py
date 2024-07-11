#Occurence of a word in a file
f=open("india.tv",'r')
s=""
c=0
l="India"
while s:
    s=f.readline()
    if l in s:
         c+=1
print(c)
