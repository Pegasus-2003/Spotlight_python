import sys
import mysql.connector as ms

mydb=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')

cur=mydb.cursor()
n=int(input('enter empno to search'))
cur.execute('select * from emp where empno='+str(n))
data=cur.fetchone()

if data!=None:
    print(*data)
else:
    print('No record found')
