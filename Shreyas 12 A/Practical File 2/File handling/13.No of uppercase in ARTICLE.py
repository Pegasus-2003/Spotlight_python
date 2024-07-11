#No of uppercase in article.txt
f=open("ARTICLE.txt",'r')
s=f.read()
c=0
for i in s:
    if i.isupper():
        c+=1
print("NUMBER OF UPPERCASE =“,c)
