#Count of uppercase and lowercase letters in a file
f=open("Answer.txt",'r')
s=f.read()
c1=0
c2=0
for i in s:
    if i.islower():
        c1+=1
    elif i.isupper():
        c2+=1
print("lower case",c1)
print("Upper case",c2)
