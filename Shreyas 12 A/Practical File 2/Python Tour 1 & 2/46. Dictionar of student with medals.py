# Dictionary with winner names and medals

medals=dict()
n=int(input("No of winners :"))
i=0
while i<n:
    a=input("Enter name :")
    b=int(input("Enter medals"))
    medals[a]=b
    i+=1
print("The dictionary is : ")
print(medals)
