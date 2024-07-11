import pickle
emp=[]
f=open("employee.dat",'rb')
emp=pickle.load(f)
print("## EMPLOYEE RECORDS ##")
print(emp)
print("---------------------------------------------------------")
f.close()
f=open("employee.dat",'wb')
found=False
en=int(input("Enter empolyee number to update :"))
for i in range(len(emp)):
    if emp[i][0]==en:
        sl=int(input("Enter new salary : "))
        emp[i][2]=sl
        found=True
        print("## RECORDS UPDATED ##")
if not found:
    print("## NO SUCH EMPLOYEE NUMBER ##")
pickle.dump(emp,f)
f.close()
f=open('employee.dat','rb')
emp=pickle.load(f)
print("## EMPLOYEE RECORDS AFTER UPDATE ##")
print(emp)
print("---------------------------------------------------------")