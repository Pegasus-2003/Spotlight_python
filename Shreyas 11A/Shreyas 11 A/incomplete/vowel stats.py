#
a =input("Enter a string")
a='space'+a+'space'
c=0
wrd=""
flag=False
for i in a:
    if flag==True:
        wrd=wrd+a
        if i=='space':
             print(wrd)
             flag=False
             wrd=""
             c+=1
if i=='space':
    if string=='a' or string=='e' or string=='i' or string=='o' or string=='u':
         flag=True
    if b<len(a-1):
         b+=1
print(c)
