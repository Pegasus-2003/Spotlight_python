#Frequency of each element of a tuple
tup=eval(input("Enter a tuple :"))
print("Element \t\t Frequency")
print()
dupl=[]
for i in tup:
    if i not in dupl:
        ele=i
        dupl.append(i)
        count=0
        for j in tup :
            if j==ele:
                count+=1
        print(ele,"\t\t",count)
