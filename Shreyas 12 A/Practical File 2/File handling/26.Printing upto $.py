#Printing  upto $
f=open("dollar.txt",'r')
s=f.read()
for i in s:
    if i=="$":
        break
    else:
        print(i,end='')
