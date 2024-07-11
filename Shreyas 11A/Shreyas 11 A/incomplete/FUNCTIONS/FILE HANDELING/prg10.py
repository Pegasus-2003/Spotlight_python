file=open("employee.txt",'w')
for i in range (5):
    a=input("Enter the employee's name: ")
    file.write (a)
    file.write('\n')
file.close()
