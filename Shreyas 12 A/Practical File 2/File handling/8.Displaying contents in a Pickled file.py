#Displaying contents in a pickle file
import pickle
f=open('search','wb')
n=int(input("Enter the number of records "))
DICTIONARY={}
for i in range(n):
    l=[]
    no=input("Enter the movie number ")
    na=input("Enter the movie name ")
    ty=input("Enter the movie type ")
    DICTIONARY["MN0"]=no
    DICTIONARY["MNAME"]=na
    DICTIONARY["MTYPE"]=ty
    pickle.dump(DICTIONARY,f)
f.close()

f=open('search','rb')
e={}
try:
    while True:
        emp=pickle.load(f)

        if emp["MTYPE"]=="comedy":
            print(emp)
except EOFError:
    f.close()
