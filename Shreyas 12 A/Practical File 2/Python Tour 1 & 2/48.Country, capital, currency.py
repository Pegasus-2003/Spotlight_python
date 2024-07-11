# Dictionary with country, capital and currency
country=dict()
n=int(input("No of entries :"))
i=0
while i<n:
    c=input("Enter  country name :")
    cap=input("Enter capital name :")
    cur=input("Enter currency name :")
    country[c]=(cap,cur)
    i+=1
for i in country:
    print("\n")
    print(i,end="  ")
    for j in country[i]:
        print(j,end="  ")
print()
