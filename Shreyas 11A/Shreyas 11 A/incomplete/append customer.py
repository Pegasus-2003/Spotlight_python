n=int(input("Enter the number of coustemers: "))
l=[]
d={}
for i in range (0,n):
    p=input("Enter the name: ")
    q=input("Enter the name of the items bought: ")
    r=int(input("Enter the total cost of the items bought: "))
    s=int(input("Enter the phone number of the custemer: "))
    l.append(q)
    l.append(r)
    l.append(s)
    d[p]=l
    l=[]
    print(d)
l2=list(d.keys())
l3=list(d.values())
print('_'*50)
print("{0:<5},{1:<10},{2:<5},{3:<10},{4:^28}".format("|",'name',"|",'[item,cost,phone no]',"|"))
for j in range (0,len(d)):
    print("{0:<5},{1:<10},{2:<5},{3:<10},{4:^28}".format("|",str(l2[j]),"|",str(l3[j]),"|"))
print('-'*50)
    
    
    
    
