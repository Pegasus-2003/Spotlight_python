import pickle
emp=[]
f=open("employee.dat",'rb')
ans='y'
print("***********************EMPLOYEE SEARCH FROM ************************")
en=int(input("Enter Employee number to search :"))
fcount=False
while True:
    try:
        emp=pickle.load(f)
    except EOFError:
        break
print("%10s"%"EMP NO","%20s"%"EMP NAME","%10s"%"EMP SALARY")
print("*********************************************************************")
for e in emp:
    if (e[0]==en):
        print("%10s"%e[0],"%20s"%e[1],"%10s"%e[2])
        fcount=True
        break
if fcount==False:
    print("##SORRY EMPLOYEE NUMBER NOT FOUND##")
f.close()