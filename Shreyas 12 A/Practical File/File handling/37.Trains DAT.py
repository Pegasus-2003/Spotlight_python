import pickle
dict={}
file=open("train.dat",'ab')
n=int(input("Enter the no of entries : "))
for i in range(n):
    no=int(input("Enter train no :"))
    from_place=input("From which place : ")
    to_place=input("To which place : ")
    dict['Tno:']=no
    dict['From:']=from_place
    dict['To:']=to_place
    pickle.dump(dict,file)
file.close()
file=open("train.dat",'rb')
data=pickle.load(file)
print(data)
    