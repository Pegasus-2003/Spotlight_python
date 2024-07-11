#Reading Binary in string
f=open('myfile.bin','rb')
s=f.read()
print(s)
s=s.decode()
print(s)
