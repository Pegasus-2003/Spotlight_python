import sys
import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=con.cursor()
a=int(input("enter sal"))
n=int(input("enter deptno"))
x="select * from emp where sal >{} and deptno = {}".format(a,n)
cur.execute(x)
data= cur.fetchall()
if data !=None:
    for row in data:
        print(*row,sep=" : ")
else:
    print("no record forund")
