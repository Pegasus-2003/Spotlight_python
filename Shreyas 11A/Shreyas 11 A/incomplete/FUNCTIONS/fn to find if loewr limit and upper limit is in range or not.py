def rang(a,b,n):
    l=[]
    for i in range (a,b+1):
        l.append(i)
    if n in l:
        print("Number exist in range. ")
    else:
        print("Number not in range.")

ul=int(input("Enter upper limit: "))
ll=int(input("Enter lower limit: "))
z=int(input("Enter the no.: "))
rang(ul,ll,z)

