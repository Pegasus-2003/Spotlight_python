#Lines starting with k
f=open("poem.txt",'r')
s=f.readlines()
for i in s:
    if i[0]=='k':
        print(i)
