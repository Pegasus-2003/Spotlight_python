# Menu driven encoder
import pickle

def create_file():
    f=open("accnt.dat",'wb')
    t = "No transaction"
    am=0
    b = 1000
    emp=[]
    N=int(input("Enter the number of records "))
    for i in range (0,N):
        acc=input("Enter acc number ")
        n=input("Enter name ")
        b=int(input("Enter current balance "))
        emp.append([acc,n,t,am,b])
        print("********")
    pickle.dump(emp,f)

def read_file():
    emp=[]
    f=open("accnt.dat",'rb')
    print("%10s" % "ACC NO", "%20s" % "NAME", "%20s" % "TRANSACTION TYPE","%10s" % "TRANSACTION AMOUNT","%10s" % "CURRENT BALANCE")
    while True:
        try:
            emp=pickle.load(f)
        except EOFError:
            break
    for e in emp:
        print("%10s" % e[0], "%20s" % e[1], "%20s" % e[2],"%10s" % e[3],"%10s" % e[4])

def update_file():
    us=input("Enter the acc no ")
    f = open("accnt.dat", 'rb')
    while True:
        try:
            emp = pickle.load(f)
        except EOFError:
            break
    nemp = []
    h = False
    for e in emp:
        if e[0]==us:
            h=True
            c=input("ENTER THE TRANSACTION TYPE ")
            if c.lower() == "credit":
                e[4] = e[4] + e[3]
                nemp.append(e)
            elif c.lower == "debit":
                if c <= 1000:
                    print("TRANSACTION NOT POSSIBLE")
                else:
                    e[4] = e[4] - e[3]
                nemp.append(e)

        else:
            nemp.append(e)
    if h==False:
        print("USER NOT VALID ")
    g=open("newp1.dat",'wb')
    pickle.dump(nemp,g)
    g.close()
    f=open("accnt.dat",'wb')
    g=open("newp1.dat",'rb')
    while True:
        try:
            emp=pickle.load(g)
        except EOFError:
            break
    pickle.dump(emp,f)




ans = 'y'
while ans.lower()=='y':
    print("1-create file")
    print("2-read file")
    print("3-update file")
    c = int(input("Enter your choice "))

    if c==1:
        create_file()
    if c==2:
        read_file()
    if c==3:
        update_file()
    ans=input("CONTINUE ?")
