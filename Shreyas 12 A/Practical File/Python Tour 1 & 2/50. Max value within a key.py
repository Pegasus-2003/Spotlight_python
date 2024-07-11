# max value within key
my_points={'a':(4,3),'b':(1,2),'c':(5,1)}
high=[0,0]
a=0
for i in range(2):
    a=0
    for j in my_points.keys():
        val=my_points[j][i]
        if a==0:
            high[i]=val
        a+=1
        if val>high[i]:
            high[i]=val;
    print("Max value at index(my_points,",i,")=",high[i])
