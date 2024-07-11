file=open("empolyee.txt",'a+')
for i in range (5):
    a=input("Enter a employee's name: ")
    file.write(a)
    file.write('\n')
file.seek(0)
print(file.read())
file.close()
