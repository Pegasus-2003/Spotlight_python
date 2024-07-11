
import sys
import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',passwd='tiger',database='class12 ')

cur=mydb.cursor()

cur.execute('select * from emp')
data=cur.fetchall()
rec=cur.rowcount
print('the total records are:',rec)

for row in data:
    
      print(*row)
      print()
