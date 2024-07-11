import sys
import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=con.cursor()
cur.execute("select * from emp  where  deptno='30' and job='SALESMAN' ")
data=cur.fetchall()
for row in data:
    print(*row, sep=' : ')
