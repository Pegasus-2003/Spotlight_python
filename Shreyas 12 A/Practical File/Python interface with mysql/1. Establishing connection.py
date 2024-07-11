import sys
import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger',database='class12')
if con.is_connected():
    print("Connection  Established")
else:
    print(" Connection  Failed ")
