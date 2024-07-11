file=input("Enter the file name :")
myfile=open(file,'r')
line=myfile.read()
word=line.split()
count=0
data=""
for i in word:
    data+=i
for j in data:
    count+=1
    if j=="$":
        break
print(count-1)
