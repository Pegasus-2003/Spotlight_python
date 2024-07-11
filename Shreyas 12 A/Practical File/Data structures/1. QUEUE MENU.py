def Empty(Q):
    if len(Q)==0:
        return True
    else:
        return False
def Enqueue(Q,item):
    Q.append(item)
    if len(Q)==1:
        front=rear=0
    else:
        rear=len(Q)-1
def Dequeue(Q):
    if Empty(Q):
        return "Underflow"
    else:
        val=Q.pop(0)
    if len(Q)==0:
        front=rear=None
    return val
def Peek(Q):
    if Empty(Q):
        return "Underflow"
    else:
        front=0
        return Q[front]
def Show(Q):
    if Empty(Q):
        print("Queue is empty \n\n\n")
    else:
        t=len(Q)-1
        print("From FRONT :=",end=' ')
        front=0
        i=front
        rear =len(Q)-1
        while (i<=rear):
            print(Q[i],"<==",end=' ')
            i+=1
        print()
        print("\n\n\n")
Q=[]
front=rear=None
while True:
    print("********* QUEUE IMPLEMENTATION *********")
    print("1.ENQUEUE")
    print("2.DEQUEUE")
    print("3.PEEK")
    print("4.SHOW")
    print("0.EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        val=int(input("Enter item to insert"))
        Enqueue(Q,val)
    elif ch==2:
        val=Dequeue(Q)
        if val=="Underflow":
            print("Queue is empty")
            print("\n")
        else:
            print("Deleted item was :",val)
            print("\n")
    elif ch==3:
        val=Peek(Q)
        if val=="Underflow":
            print("Queue is empty \n\n\n")
        else:
            print("Topmost item is :", val)
            print("\n")
    elif ch==4:
        Show(Q)
    elif ch==0:
        break
