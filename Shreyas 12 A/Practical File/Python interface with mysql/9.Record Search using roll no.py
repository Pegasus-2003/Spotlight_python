 import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='class12’)
cur=mydb.cursor()
r=int(input('enter roll no'))
cur.execute('select*from std where rollno={}'.format(r))
data=cur.fetchall()
print(data)
if data !=None:
    print('record found - Details are. . . .')
    for row in data:
        print(*row,sep=' : ')
    ans=input('do u wish to update the class')
    if ans=='y':
        c=int(input('Enter new class'))
        cur.execute('update std set class= {} where rollno = {}'.format(c,r))
        con.commit()
        print('$$ Record updated##')
    else:
        print('thank you')
else:
    print('sorry no record found')
con.close()
