with open("Telephone.txt","w") as f1:
    n=int(input("enter the no of telephone number"))
    while n>0:
        name=input("Name:")
        no=input("Telephone number:")
        n-=1
        rec=name+" "+no 
        f1.write(rec)
        f1.write("\n")

file=open("Telephone.txt","r")
for line in file:
    word=line.split()
    print(word[0],'\t\t',word[1])