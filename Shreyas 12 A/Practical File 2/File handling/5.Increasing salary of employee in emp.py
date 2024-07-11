#Increasing salasry of employess from emp1.dat
import pickle
f=open("emp1.bin",'wb+')
n=int(input("Enter the number of employees"))
for i in range (n):
    emp={}
    no=int(input("Enter the emp no "))
    sal=int(input("Enter the salary "))
    emp['NUMBER']=no
    emp['SALARY']=sal
    pickle.dump(emp,f)
f.close()

f=open("emp1.bin",'rb+')
emp1={}
try:
    while True:
        emp1=pickle.load(f)
        if emp1['NUMBER']==1251:
            emp1['SALARY']+=2000
        print(emp1)
except EOFError:
    f.close()
