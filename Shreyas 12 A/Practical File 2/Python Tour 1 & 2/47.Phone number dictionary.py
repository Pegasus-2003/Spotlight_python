# Dictionary with names and numbers
phone=dict()
n=int(input("No of entries :"))
i=0
while i<n:
    a=input("Enter name :")
    b=int(input("Enter number"))
    phone[a]=b
    i+=1
l=phone.keys()
x=input("enter name to be searched ")
for i in l:
    if i==x:
        print(x,phone[i])
        break
    else:
        print("Entry not found")
