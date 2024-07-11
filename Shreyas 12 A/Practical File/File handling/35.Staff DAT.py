# Staff DAT
import pickle

file=open("staff.dat",'a+b')
staff={}
n=int(input("Input number of entries :"))
for i in range(n):
    code="Staff code:" + input("Enter the staff code :")
    name="Staff name:" + input("Enter the staff name :")
    staff[code]=name
pickle.dump(staff,file)
file.seek(0,0)
data=pickle.load(file)
print("%5s"%"Staff code","%20s"%"Staff Name")
print("***********************************")
for i in data:
    print("%5s"%i[11:],"%25s"% data[i][5:])
file.close()

file1=open("Staff.dat",'rb')
search=input("Enter the code that u want to search :")
data=pickle.load(file1)
for i in data:
    if i[11:] == search:
        print("Record found ")
        print("%10s"%"Staff code","%20s"%"Staff Name")
        print("*********************************************************")
        print("%10s"%i[11:],"%20s"% data[i][5:])
        break
else:
    print("Record not found ")
file1.close()
    
