import pdb
a=0
b=1
print(a)
print(b)
for i in range(5):
    pdb.set_trace()
    c=a+b
    print(c,end=" ")
    b=c
    a=b
    
