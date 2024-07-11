import pickle

def create_file(n):
    with open("account.dat",'w+b') as f:
        for i in range(n):
            accno=input("Enter ACC No :")
            name=input("Enter name :")
            bal=int(input("Enter current balance :"))
            pickle.dump([accno,name,bal],f)
            
def read_file():
    c=0
    with open("account.dat",'rb') as f:
        while f:
            c=c+1
            try:
                r=pickle.load(f)
                print(r)
            except EOFError :
                if c==0:
                    print("No records ")
                else:
                    break
def update_file():
    acc=[]
    f=open("account.dat",'rb')
    acc=pickle.load(f)
    f.close()
    f=open("account.dat",'wb')
    found=False
    accno=int(input("Enter account number to update :"))
    if acc[i][0]==accno:
        newbal=bal+(bal/10)
        acc[i][2]=newbal
        found=True
        print("updated")
    if not found:
        print("No such accno")
    pickle.dump(acc,f)
    f.close()
    f=open("account.dat",'rb')
    acc=pickle.load(f)
    print(acc)
print("1.create file")
print("2.read file")
print("3.update file")
c=int(input("Enter option :"))
if c==1:
    A=int(input("Enter number of records :"))
    creat_file(A)
elif c==2:
    read_file()
elif c==3:
    update_file()

        