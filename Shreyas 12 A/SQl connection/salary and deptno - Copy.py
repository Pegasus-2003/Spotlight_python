import sys
import mysql.connector as ms
con=ms.connect(host="localhost",user="root",passwd="tiger",database="class12")
cur=con.cursor()
n=int(input("Enter the salary amount"))
a=int(input("Enter deptno"))
cur.execute("select * from emp where sal>{} and deptno ={}".format(n,a))
data=cur.fetchall()
rec=cur.rowcount
if data !=None:
    for row in data:
        print(*row,sep=" : ")
else:
    print("Record Not found")
