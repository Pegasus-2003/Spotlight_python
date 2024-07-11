import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=con.cursor()
n=int(input('enter sal'))
cur.execute('select * from emp where sal>'+str(n))
data=cur.fetchall()
rec=cur.rowcount
if data != None:
    for i in data:
        print(*i,sep=':')
else:
    print('no record found')
