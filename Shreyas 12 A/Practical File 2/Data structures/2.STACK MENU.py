def empty(s):
    if len(s)==0:
        return True
    else:
        return False

def Push(l,k):
    l.append(k)
    top=len(s)-1

def pop(s):
    if empty(s):
        return "Underflow"
    else:
        v=s.pop()
        if len(s)==0:
            top= None
        else:
            top=len(s)-1
        return v

def Peek(s):
    if empty(s):
        return "Underflow"
    else:
        top=len(s)-1
        return s[top]

def Show(s):
    if empty(s):
        print("Stack is empty. Nothing to delete \n\n\n")
    else:
        top=len(s)-1
        print("From Top :=",end=' ')
        while (top>=0):
            print(s[top],"<=",end=' ')
            top-=1
        print()
        print("\n\n\n")
s=[]
top=None
while True:
    print(" **********STACK IMPLEMETATIONS ***********")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    print("0.EXIT")
    ch=int(input("Enter your choice "))
    if ch==1:
        vl=int(input("Enter item to insert "))
        print("\n\n\n")
        Push(s,vl)
    elif ch==2:
        val=pop(s)
        if val =="Underflow":
            print("Stack is empty")
            print("\n\n\n")
        else:
            print("Deleted Item :",val)
            print("\n\n\n")
    elif ch==3:
        val=Peek(s)
        if val=="Uderfolw":
            print("Stack is empty")
        else:
            print("Topmost item is :",val)
            print("\n\n\n")
    elif ch==4:
        Show(s)
    elif ch==0:
        print("Bye")
        break
