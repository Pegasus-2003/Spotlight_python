import sys
import mysql.connector as ms

mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='class12’)

cur=mydb.cursor()
cur.execute('select sum(sal) as "total" from emp where deptno=10')

data=cur.fetchall()
for row in data:
    print(*row,sep=' : ')
