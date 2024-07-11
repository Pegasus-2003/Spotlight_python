import sys
import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=con.cursor()
cur.execute("select * from emp  where  ename like 'M%'  ")
data=cur.fetchall()
for row in data:
    print(*row, sep=' : ')
