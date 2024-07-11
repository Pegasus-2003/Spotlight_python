#Merging two text files
n=input("Enter the name of the new file ")
n1=input("Enter the 1st old file ")
n2=input("Enter the 2nd old file ")
f1=open(n1,'r')
s1=f1.read()
f2=open(n2,'r')
s2=f2.read()
f=open(n,'w')
s3=s1+s2
f.write(s3)
