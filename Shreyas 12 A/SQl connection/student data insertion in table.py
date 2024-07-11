import sys
import mysql.connector as ms
con=ms.connect(host="localhost",user="root",passwd="tiger",database="class12")
cur=con.cursor()
ans='y'
while ans=="y":
    r=int(input(" Enter roll no :"))
    n=input("Enter name :")
    c=int(input("Enter the class :"))
    g=input("Enter gender :")
    cur.execute("Insert into std values({0},{1},{2},{3})".format(r,n,c,g))
    con.commit()
    print("Record saved ")
    ans=input("Do u want to continue ?")
    
    
