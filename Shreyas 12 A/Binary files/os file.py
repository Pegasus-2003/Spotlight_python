import os
size_of_rec=20
size=os.path.getsize('Names.dat')
print("Size of file :",size)
num_rec=int(size/size_of_rec)
print("Number of records :",num_rec)
with open('Names.dat','rb') as f:
    n=input('Enter name to search')
    n=n.encode()
    position=0
    found=False
    for i in range(num_rec):
        f.seek(position)
        str=f.read(20)
        if n in str:
            print('Found at record :',i+1)
            found=True
        postion+=size_pf_rec
    if not found:
        print('Name not found')
        