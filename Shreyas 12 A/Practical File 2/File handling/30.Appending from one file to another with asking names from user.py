#Appending from one file to another with asking names from user
n1=input("Enter the name of the original file ")
n2=input("Enter the name of the file where to be copied ")
while True:
    try:
        f=open(n1,'r')
        s=f.read()
        g = open(n2, 'w')
        g.write(s)
        break
    except:
        print("check the file names")
        break
