with open("sports.dat","w") as f1:
    n=int(input("enter the no of records"))
    while n>0:
        event=input("event:")
        name=input("name:")
        n-=1
        rec=event+" "+name 
        f1.write(rec)
        f1.write("\n")
        print("record is added")

with open("sports.dat","r") as f1:
    with open("athletics.dat","w") as f2:
        reader=f1.read().split()
        for i in range(0,len(reader)):
            if reader[i]=="athletics":
                f2.write(reader[i]+" "+reader[i+1])
                f2.write("\n")
            else:
                continue