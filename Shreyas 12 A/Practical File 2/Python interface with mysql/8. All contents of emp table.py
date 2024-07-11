import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=con.cursor()
cur.execute('select * from emp')
data = cur.fetchall()
if data != None:
    for i in data:
        print(*i,sep=':')
else:
    print('no record found')
