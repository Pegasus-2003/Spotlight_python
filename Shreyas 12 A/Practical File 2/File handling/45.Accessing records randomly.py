#Accesing records randomly
s=20
n=int(input("Enter the record number "))
with open("NAMES.dat",'rb') as f:
    f.seek(s*(n-1))
    k=f.read(s)	
    if len(k)==0:
        print("no record")
    else:
        print(k.decode())

