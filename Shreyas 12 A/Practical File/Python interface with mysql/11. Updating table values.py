import sys
import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=mydb.cursor()
print('welcome to std database')
ans='y'
while ans=='y':
    r=int(input('enter roll no'))
    n=input('Enter name')
    c=int(input('Enter class'))
    s=input('enter sex')
    query="insert into std values({0},{1},{2},{3})".format(r,n,c,s)
    cur.execute(query)
    con.commit()
    print('$$ Record Saved ##')
    ans=input('do you want to add another record')
