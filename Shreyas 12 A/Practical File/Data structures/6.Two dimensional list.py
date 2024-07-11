# 2 dimensional list
r=int(input("Enter the no of rows "))
c=int(input("Enter the no fo columns "))
mat=[]
for i in range(r):
    R=[]
    for j in range(c):
        n=int(input("Enter the value to be stored at index ["+str(i)+","+str(j)+"]"))
        R.append(n)
    mat.append(R)
for i in range(r):
    for j in range (c):
        print(mat[i][j],end="")
    print()
print()
