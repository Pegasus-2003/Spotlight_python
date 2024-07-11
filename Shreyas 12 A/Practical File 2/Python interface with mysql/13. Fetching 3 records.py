import sys
import mysql.connector as ms

mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='class12 ')

cur=mydb.cursor()
cur.execute('select * from emp')

data=cur.fetchmany(3)
rec=cur.rowcount
print('Total records are',rec)
for row in data:
    print(*row,sep=' : ')
