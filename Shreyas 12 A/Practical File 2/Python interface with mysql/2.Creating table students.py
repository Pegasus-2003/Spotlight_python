import mysql.connector as ms
import sys
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
cur=con.cursor()	
print("Welcome to student database")
cur.execute("DROP TABLE IF EXISTS std")
cur.execute("CREATE TABLE std (rollno decimal(3,0),name varchar(10), class decimal(2,0), sex varchar(4))")
con.commit()

